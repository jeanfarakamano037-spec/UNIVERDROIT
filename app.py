from flask import Flask, jsonify, request
import json, os, uuid
from datetime import datetime
app = Flask(__name__)

# ===== GEMINI AI - FAQ =====
def ask_gemini(q):
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key: return None
    try:
        import json as js, urllib.request
        prompt = f"Tu es professeur de droit guineen et OHADA. Reponds en francais simple, avec articles, procedure Conakry, exemples Guinee. Question: {q}. Max 300 mots."
        data = js.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
        req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}", data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=25) as r:
            res = js.loads(r.read())
            return res["candidates"][0]["content"]["parts"][0]["text"] + "\n\nSource: AI Gemini - Droit Guineen & OHADA"
    except Exception: return None

def load_j(f,d):
    if not os.path.exists(f): return d
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return d
def save_j(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

# ===== TES COURS RECUPERES DE TON FICHIER REACT =====
# Structure: Licence -> Matiere (dossier) -> Programme -> Chapitre -> Section -> Sous-section -> Lecon
def matiere(nom, code, desc, prof, chapitres):
    prog=[]
    for i,ch in enumerate(chapitres):
        prog.append({"titre": f"Chapitre {i+1}: {ch}", "sections":[
            {"titre": f"Section 1: {ch}", "sous_sections":[
                {"titre": f"Sous-section 1: Les notions essentielles de {ch.lower()}", "lecon": f"{desc} Prof: {prof}. Chapitre: {ch}. Notions essentielles: definition, conditions, exemples guineens et OHADA. Pour approfondir, pose ta question dans FAQ AI."},
                {"titre": "Sous-section 2: Les conditions d'application", "lecon": f"Conditions d'application de: {ch}. Qui ? Quoi ? Ou ? Quand ? Procedure a Conakry: mise en demeure 8j huissier 50k, conciliation, TPI, appel 1 mois, cassation 2 mois / CCJA si OHADA."}
            ]}
        ]})
    return {"id": code, "matiere": nom, "prof": prof, "desc": desc, "icon": "📖", "programme": prog}

COURS = {
"L1": [
 matiere("Introduction au Droit","L1-01","La notion, les sources et l'organisation du droit.","Pr. N'Guessan",["Notion de droit et caracteres de la regle","Les sources du droit","L'organisation judiciaire","La preuve et les personnes"]),
 matiere("Droit Constitutionnel","L1-02","Constitution, Etat et separation des pouvoirs.","Dr. Koffi",["L'Etat et la Constitution","La separation des pouvoirs","Les droits fondamentaux","Les regimes politiques"]),
 matiere("Droit Civil 1 - Personnes & Famille","L1-03","Personnalite, filiation, mariage et regimes.","Pr. Diallo",["La personnalite juridique","Le mariage et le divorce","La filiation","La protection des majeurs"]),
 matiere("Histoire du Droit","L1-04","Des droits antiques aux codifications.","Dr. Traore",["Les droits anciens","Le droit romain","L'Ancien Regime","Les grandes codifications"]),
 matiere("Droit Administratif 1","L1-05","Administration, acte administratif et service public.","Pr. Kone",["L'administration et ses missions","L'acte administratif","Le service public","Le controle de l'administration"]),
 matiere("Economie Politique","L1-06","Marche, Etat et politiques publiques.","Dr. Mensah",["Les acteurs economiques","Le marche et la concurrence","La monnaie et l'inflation","La croissance et le developpement"]),
 matiere("Relations Internationales","L1-07","Etats, organisations et ordre international.","Pr. Diop",["Les acteurs internationaux","La souverainete","Les organisations internationales","La paix et la securite"]),
 matiere("Methodologie Juridique","L1-08","Dissertation, commentaire et cas pratique.","Dr. Yao",["La dissertation juridique","Le commentaire d'arret","Le cas pratique","La recherche documentaire"]),
],
"L2": [
 matiere("Droit des Obligations","L2-01","Contrat, responsabilite et quasi-contrats.","Pr. N'Guessan",["La formation du contrat","L'execution du contrat","La responsabilite civile","Les quasi-contrats"]),
 matiere("Droit Penal General","L2-02","Infraction, responsabilite et peine.","Dr. Koffi",["L'infraction","L'auteur et le complice","La responsabilite penale","La peine et son application"]),
 matiere("Droit Administratif 2","L2-03","Responsabilite et contrats administratifs.","Pr. Kone",["La responsabilite administrative","Les contrats administratifs","Le domaine public","Le recours pour exces de pouvoir"]),
 matiere("Droit des Affaires","L2-04","Commercant, actes de commerce et fonds.","Dr. Mensah",["Le commercant","Les actes de commerce","Le fonds de commerce","Les effets de commerce"]),
 matiere("Droit Fiscal","L2-05","Impot, assiette et controle fiscal.","Pr. Diallo",["Les principes de l'impot","L'impot sur le revenu","La TVA","Le controle et le contentieux"]),
 matiere("Droit International Public","L2-06","Traites, responsabilite et juridictions.","Pr. Diop",["Les sources du droit international","Les traites","La responsabilite internationale","Les juridictions internationales"]),
 matiere("Droit Civil 2 - Biens","L2-07","Propriete, possession et demembrements.","Dr. Traore",["La propriete","La possession","L'usufruit et la servitude","La copropriete"]),
 matiere("Procedure Civile","L2-08","Action, instance et voies de recours.","Dr. Yao",["L'action en justice","L'instance","Le jugement","Les voies de recours"]),
],
"L3": [
 matiere("Droit des Contrats Speciaux","L3-01","Vente, bail, mandat et contrats nommes.","Pr. N'Guessan",["La vente","Le bail","Le mandat","Le pret et le depot"]),
 matiere("Droit Penal Special","L3-02","Atteintes aux personnes, aux biens et a la societe.","Dr. Koffi",["Les atteintes aux personnes","Les atteintes aux biens","Les infractions economiques","Les infractions contre l'Etat"]),
 matiere("Droit du Travail","L3-03","Contrat de travail, licenciement et negociation.","Pr. Kone",["Le contrat de travail","La duree et la remuneration","Le licenciement","Les relations collectives"]),
 matiere("Droit des Societes","L3-04","Creation, fonctionnement et dissolution.","Dr. Mensah",["Les formes de societes","La creation de la societe","Le fonctionnement","La dissolution et la liquidation"]),
 matiere("Droit International Prive","L3-05","Conflits de lois et de juridictions.","Pr. Diop",["Le conflit de lois","Le conflit de juridictions","La nationalite","La condition des etrangers"]),
 matiere("Procedure Penale","L3-06","Enquete, poursuite et jugement penal.","Dr. Yao",["L'enquete","La poursuite","L'instruction","Le proces penal"]),
 matiere("Droit de l'Environnement","L3-07","Pollution, responsabilite et protection.","Pr. Diallo",["Les principes environnementaux","La pollution","La responsabilite ecologique","Les aires protegees"]),
 matiere("Droit OHADA","L3-08","Actes uniformes et CCJA.","Pr. Traore",["Presentation de l'OHADA","Les Actes uniformes","La CCJA","L'arbitrage OHADA"]),
]
}

OHADA = [
 {"id":"ohada","matiere":"OHADA - 10 Actes Uniformes","icon":"⚖️","programme":[
  {"titre":"Chapitre 1: Presentation de l'OHADA","sections":[{"titre":"Section 1: Presentation","sous_sections":[{"titre":"Sous-section 1: Definition","lecon":"Organisation pour l'Harmonisation en Afrique du Droit des Affaires : 17 Etats, un droit harmonise pour securiser affaires, investissements et echanges."}]}]},
  {"titre":"Chapitre 2: Droit commercial general","sections":[{"titre":"Section 1: Commercant","sous_sections":[{"titre":"Sous-section 1: RCCM","lecon":"Commercant, registre du commerce, bail commercial, intermediaires et vente commerciale. Immatriculation et comptabilite obligatoires."}]}]},
  {"titre":"Chapitre 3: Droit des societes & GIE","sections":[{"titre":"Section 1: Societes","sous_sections":[{"titre":"Sous-section 1: Types","lecon":"SNC, SARL, SA, SAS. Constitution, apports, organes, responsabilite dirigeants et dissolution. SARL 1M, SA 10M."}]}]},
  {"titre":"Chapitre 4: Suretes","sections":[{"titre":"Section 1: Suretes","sous_sections":[{"titre":"Sous-section 1: Caution Hypotheque","lecon":"Cautionnement, nantissement, gage, hypotheque, droit de retention. La surete garantit paiement dette par bien ou garant."}]}]},
  {"titre":"Chapitre 5: Procedures collectives","sections":[{"titre":"Section 1: Redressement","sous_sections":[{"titre":"Sous-section 1: Objectif","lecon":"Reglement preventif, redressement judiciaire et liquidation. Sauvegarder entreprise, maintenir emploi et payer creanciers."}]}]},
  {"titre":"Chapitre 6: Arbitrage","sections":[{"titre":"Section 1: Arbitrage","sous_sections":[{"titre":"Sous-section 1: Sentence","lecon":"Convention d'arbitrage, tribunal arbitral, sentence et recours CCJA. Rapidite, confidentialite, execution facilitee."}]}]},
  {"titre":"Chapitre 7: Comptabilite","sections":[{"titre":"Section 1: SYSCOHADA","sous_sections":[{"titre":"Sous-section 1: Plan comptable","lecon":"Plan comptable OHADA, etats financiers, audit. Transparence protege associes, creanciers, investisseurs."}]}]},
  {"titre":"Chapitre 8: Transport","sections":[{"titre":"Section 1: Transport route","sous_sections":[{"titre":"Sous-section 1: Responsabilite","lecon":"Contrat de transport, responsabilite transporteur, delais et indemnisation perte ou avarie."}]}]},
  {"titre":"Chapitre 9: Mediation","sections":[{"titre":"Section 1: Mediation","sous_sections":[{"titre":"Sous-section 1: Accord","lecon":"Processus amiable guide par tiers neutre. Preserve relation et aboutit a accord executoire."}]}]},
  {"titre":"Chapitre 10: La CCJA","sections":[{"titre":"Section 1: CCJA","sous_sections":[{"titre":"Sous-section 1: Cassation","lecon":"Cour Commune de Justice et d'Arbitrage : interpretation uniforme des Actes uniformes et juge en cassation. Abidjan, 13 juges."}]}]},
 ]}
]

DICT = [
 {"t":"Abus de droit","d":"Exercice d'un droit pour causer prejudice anormal a autrui. Ex: mur pour priver voisin de lumiere."},
 {"t":"Acte juridique","d":"Manifestation de volonte pour produire effets de droit : contrat, testament, donation."},
 {"t":"Amnistie","d":"Loi qui efface caractere infractionnel de certains faits."},
 {"t":"Appel","d":"Voie de recours pour faire rejuger affaire en fait et en droit. Delai 1 mois."},
 {"t":"Arret","d":"Decision cour d'appel, Cour supreme ou CCJA."},
 {"t":"Assignation","d":"Acte demandeur appelle personne a comparaitre devant tribunal, signifie par huissier."},
 {"t":"Bail","d":"Contrat qui donne jouissance chose moyennant loyer."},
 {"t":"Cassation","d":"Annulation par juridiction supreme d'une decision en violation du droit."},
 {"t":"Contrat","d":"Accord de volontes pour creer obligations. 4 conditions: consentement, capacite, objet, cause."},
 {"t":"Juge","d":"Magistrat qui tranche litiges, TPI, Cour Appel, Supreme."},
 {"t":"OHADA","d":"17 pays, 10 Actes Uniformes, CCJA Abidjan."},
 {"t":"SARL","d":"1-100 associes, capital 1M, responsabilite limitee."},
 {"t":"Titre Foncier","d":"Seul papier propriete terrain Guinee, Conservation Kaloum, 2-5M."},
]
DICT += load_j("dict_extra.json", [])

QUIZ = {
"L1": [{"q":"Constitution 2020 Guinee = quelle Republique?","o":["3e","4e","5e"],"r":1,"e":"4e Republique 2020"},{"q":"Garde a vue max?","o":["24h","48h renouvelable 96h","7j"],"r":1,"e":"48h x2 = 96h"},{"q":"OHADA pays?","o":["10","17","54"],"r":1,"e":"17 pays"}],
"L2": [{"q":"Crime juge par?","o":["TPI","Cour Assises","Supreme"],"r":1,"e":"Assises jury"},{"q":"SARL capital min?","o":["100k","1M","10M"],"r":1,"e":"1M OHADA"}],
"L3": [{"q":"Titre Foncier ou?","o":["Mairie","Conservation Kaloum","APIP"],"r":1,"e":"Conservation Kaloum"}],
"OHADA": [{"q":"OHADA = ?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Harmonisation Droit Affaires Afrique"}]
}
FAQ_BASE = [("juge","Juge = magistrat qui tranche litiges, TPI, Cour Appel, Supreme."),("avocat","Avocat = Barreau Kaloum, consultation 200-500k."),("sarl","SARL: APIP 1,5M 48h, capital 1M, RCCM 500k."),("terrain","Titre Foncier seul papier propriete. Conservation Kaloum 2-5M.")]
def moteur_faq(q):
    rep = ask_gemini(q)
    if rep: return rep
    ql=q.lower()
    for k,a in FAQ_BASE:
        if k in ql: return a
    return f"Pour '{q}': Dis-moi plus: civil, penal, commerce OHADA, travail, foncier?"

@app.route("/")
def home():
    return """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DROIT224 - Universite Droit</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial}.header{text-align:center;padding:14px;background:#0a0a2a;border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}.tabs{display:flex;gap:4px;padding:6px;background:#0a0a1a;overflow-x:auto;position:sticky;top:95px;z-index:20}.tabs button{padding:8px 11px;border-radius:18px;border:1px solid #222;background:#151530;color:#aaa;font-size:10px;font-weight:800;white-space:nowrap}.tabs button.active{background:#f9c00f;color:#000}.view{display:none;padding:10px}.view.active{display:block}.card{background:#10102a;border:1px solid #1a1a3a;border-radius:12px;padding:12px;margin:8px 0;cursor:pointer}input,select,textarea{width:100%;padding:9px;margin:4px 0;border-radius:8px;border:1px solid #222;background:#111;color:#fff}.btn{padding:9px 14px;border-radius:18px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer}.small{font-size:13px;color:#ddd;line-height:1.7;white-space:pre-wrap}.lecon{background:#0a1a0a;border:2px solid #76ff03;padding:14px;border-radius:10px;margin-top:10px}.licence-card{background:linear-gradient(135deg,#1a1a4a,#0a0a2a);border:2px solid #f9c00f;padding:18px;border-radius:16px;margin:10px 0;text-align:center;cursor:pointer}</style></head><body>
<div class="header"><h1 style="color:#f9c00f;font-size:28px">DROIT224</h1><p style="font-size:9px;color:#aaa">UNIVERSITE DROIT - L1 L2 L3 - OHADA - DICTIONNAIRE - QUIZ - FAQ AI - DOSSIER - CERCLE</p><button class="btn" onclick="downloadApp()" style="margin-top:8px">📥 TELECHARGER L'APP</button></div>
<div class="tabs"><button class="active" onclick="show('cours')">📚 COURS</button><button onclick="show('ohada')">⚖️ OHADA</button><button onclick="show('dict')">📖 DICTIONNAIRE</button><button onclick="show('quiz')">🏆 QUIZ</button><button onclick="show('faq')">🤖 FAQ AI</button><button onclick="show('dossier')">📂 DOSSIER</button><button onclick="show('cercle')">💬 CERCLE</button><button onclick="show('depot')">📤 DEPOT</button></div>
<div id="cours" class="view active"><h2>📚 COURS</h2><div id="licences"></div><div id="matieres"></div><div id="detail"></div></div>
<div id="ohada" class="view"><h2>⚖️ OHADA</h2><div id="ohadaList"></div><div id="ohadaDetail"></div></div>
<div id="dict" class="view"><h2>📖 Dictionnaire A-Z + Termes</h2><input id="searchDict" placeholder="Cherche: juge, SARL..." oninput="filterDict()"><div id="dictList"></div></div>
<div id="quiz" class="view"><h2>🏆 QUIZ - Badge apres 20 questions</h2><select id="quizLic"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">Commencer</button><div id="quizBox"></div></div>
<div id="faq" class="view"><h2>🤖 FAQ AI</h2><input id="faqQ" placeholder="Ex: c'est qui le juge?"><button class="btn" onclick="askFaq()">Demander a AI</button><div id="faqAns" class="small"></div></div>
<div id="dossier" class="view"><h2>📂 DOSSIER JUSTICE</h2><input id="dNom" placeholder="Ton nom"><select id="dRang"><option>Etudiant</option><option>Prof</option><option>Enseignant</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option><option>Citoyen</option></select><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol</option><option>Viol</option><option>Contrat</option><option>Crime</option><option>Succession</option><option>Autre</option></select><textarea id="dCas" placeholder="Decris ton cas..."></textarea><button class="btn" onclick="submitDossier()">Soumettre</button><div id="dossierList"></div></div>
<div id="cercle" class="view"><h2>💬 CERCLE</h2><input id="cNom" placeholder="Ton nom"><select id="cRang"><option>Etudiant</option><option>Prof</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option></select><textarea id="cMsg" placeholder="Parle droit ici..."></textarea><button class="btn" onclick="sendCercle()">Envoyer</button><div id="cercleList"></div></div>
<div id="depot" class="view"><h2>📤 DEPOT COURS</h2><input id="pNom" placeholder="Ton nom"><select id="pRang"><option>Prof</option><option>Enseignant</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option><option>Etudiant</option></select><input id="pTitre" placeholder="Titre du cours"><input id="pLic" placeholder="Licence: L1 / L2 / L3 / OHADA"><textarea id="pDesc" placeholder="Description..."></textarea><button class="btn" onclick="submitDepot()">Deposer</button><div id="depotList"></div></div>
<script>
let COURS={},OHADA=[],DICT=[],QUIZ={};
function show(id){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active')}
async function load(){let r=await fetch('/api/data');let d=await r.json();COURS=d.cours;OHADA=d.ohada;DICT=d.dict;QUIZ=d.quiz;renderLic();renderOhada();renderDict();loadDossiers();loadCercle();loadDepot()}
function renderLic(){let h='';for(let lic in COURS){h+=`<div class="licence-card" onclick="showMat('${lic}')"><h2>🎓 LICENCE ${lic}</h2><p>${COURS[lic].length} matieres</p></div>`}document.getElementById('licences').innerHTML=h}
function showMat(lic){let h=`<h3>Licence ${lic}</h3>`;COURS[lic].forEach((m,i)=>{h+=`<div class="card" onclick="showProg('${lic}',${i})">📂 ${m.icon} ${m.matiere} - ${m.prof}<br><small>${m.desc}</small></div>`});document.getElementById('matieres').innerHTML=h;document.getElementById('detail').innerHTML=''}
function showProg(lic,mi){let m=COURS[lic][mi];let h=`<h3>📂 ${m.matiere} - ${m.prof}</h3><p>${m.desc}</p>`;m.programme.forEach(ch=>{h+=`<div class="card"><b>${ch.titre}</b>`;ch.sections.forEach(s=>{h+=`<p>📁 ${s.titre}</p>`;s.sous_sections.forEach(ss=>{h+=`<div style="margin-left:12px"><b>📄 ${ss.titre}</b><div class="lecon small">${ss.lecon}</div></div>`})});h+=`</div>`});document.getElementById('detail').innerHTML=h}
function renderOhada(){let h='';OHADA.forEach((m,i)=>{h+=`<div class="card" onclick="showOhada(${i})">📂 ${m.icon} ${m.matiere}</div>`});document.getElementById('ohadaList').innerHTML=h}
function showOhada(i){let m=OHADA[i];let h=`<h3>${m.matiere}</h3>`;m.programme.forEach(ch=>{h+=`<div class="card"><b>${ch.titre}</b>`;ch.sections.forEach(s=>{h+=`<p>${s.titre}</p>`;s.sous_sections.forEach(ss=>{h+=`<div class="lecon small"><b>${ss.titre}</b><br>${ss.lecon}</div>`})});h+=`</div>`});document.getElementById('ohadaDetail').innerHTML=h}
function renderDict(){document.getElementById('dictList').innerHTML=DICT.map(d=>`<div class="card"><b>${d.t}</b><div class="small">${d.d}</div></div>`).join('')}
function filterDict(){let q=document.getElementById('searchDict').value.toLowerCase();let f=DICT.filter(d=>d.t.toLowerCase().includes(q));document.getElementById('dictList').innerHTML=f.map(d=>`<div class="card"><b>${d.t}</b><div class="small">${d.d}</div></div>`).join('')}
let qi=0,score=0,cur=[];
function startQuiz(){let lic=document.getElementById('quizLic').value;cur=QUIZ[lic]||[];qi=0;score=0;showQ()}
function showQ(){if(qi>=cur.length){let badge=score>=3?'🏆 BADGE OR - EXPERT DROIT':score>=1?'🥈 BADGE ARGENT':'📜 Continue';document.getElementById('quizBox').innerHTML=`<h3>Score: ${score}/${cur.length}</h3><div>${badge}</div>`;return}let q=cur[qi];document.getElementById('quizBox').innerHTML=`<div class="card"><b>Q${qi+1}: ${q.q}</b>${q.o.map((o,i)=>`<button class="btn" style="display:block;margin:4px" onclick="ans(${i})">${o}</button>`).join('')}</div>`}
function ans(i){if(i==cur[qi].r)score++;alert(cur[qi].e);qi++;showQ()}
async function askFaq(){let q=document.getElementById('faqQ').value;let r=await fetch('/api/faq?q='+encodeURIComponent(q));let d=await r.json();document.getElementById('faqAns').innerText=d.answer}
async function submitDossier(){let b={nom:document.getElementById('dNom').value,rang:document.getElementById('dRang').value,type:document.getElementById('dType').value,cas:document.getElementById('dCas').value};await fetch('/api/dossier',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadDossiers()}
async function loadDossiers(){let r=await fetch('/api/dossier');let d=await r.json();document.getElementById('dossierList').innerHTML=d.map(x=>`<div class="card"><b>${x.type} - ${x.nom} (${x.rang})</b><div class="small">${x.cas}</div><div>${(x.aides||[]).map(a=>`<p>💬 ${a.nom} (${a.rang}): ${a.msg}</p>`).join('')}</div><input id="aide-${x.id}" placeholder="Aider..."><button class="btn" onclick="aider('${x.id}')">Aider</button></div>`).join('')}
async function aider(id){let msg=document.getElementById('aide-'+id).value;let nom=document.getElementById('dNom').value||'Anonyme';let rang=document.getElementById('dRang').value;await fetch('/api/dossier/aide',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,nom,rang,msg})});loadDossiers()}
async function sendCercle(){let b={nom:document.getElementById('cNom').value,rang:document.getElementById('cRang').value,msg:document.getElementById('cMsg').value};await fetch('/api/cercle',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadCercle()}
async function loadCercle(){let r=await fetch('/api/cercle');let d=await r.json();document.getElementById('cercleList').innerHTML=d.map(x=>`<div class="card"><b>${x.nom} (${x.rang})</b><div class="small">${x.msg}</div><small>${x.date||''}</small></div>`).join('')}
async function submitDepot(){let b={nom:document.getElementById('pNom').value,rang:document.getElementById('pRang').value,titre:document.getElementById('pTitre').value,lic:document.getElementById('pLic').value,desc:document.getElementById('pDesc').value};await fetch('/api/depot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadDepot()}
async function loadDepot(){let r=await fetch('/api/depot');let d=await r.json();document.getElementById('depotList').innerHTML=d.map(x=>`<div class="card"><b>📄 ${x.titre} - ${x.lic}</b><div class="small">Par ${x.nom} (${x.rang}) - ${x.desc}</div></div>`).join('')}
function downloadApp(){alert('Chrome -> Menu -> Ajouter a ecran accueil. Ton app devient comme Play Store!')}
load()
</script></body></html>
"""

@app.route("/api/data")
def api_data(): return jsonify({"cours":COURS,"ohada":OHADA,"dict":DICT,"quiz":QUIZ})
@app.route("/api/faq")
def api_faq(): return jsonify({"answer": moteur_faq(request.args.get("q",""))})
@app.route("/api/dossier", methods=["GET","POST"])
def api_dossier():
    arr=load_j("dossiers.json",[])
    if request.method=="POST":
        b=request.get_json() or {}; b["id"]=str(uuid.uuid4())[:8]; b["aides"]=[]; arr.append(b); save_j("dossiers.json",arr); return jsonify({"ok":True})
    return jsonify(arr)
@app.route("/api/dossier/aide", methods=["POST"])
def api_aide():
    arr=load_j("dossiers.json",[]); b=request.get_json() or {}
    for x in arr:
        if x["id"]==b.get("id"): x.setdefault("aides",[]).append({"nom":b.get("nom"),"rang":b.get("rang"),"msg":b.get("msg")})
    save_j("dossiers.json",arr); return jsonify({"ok":True})
@app.route("/api/cercle", methods=["GET","POST"])
def api_cercle():
    arr=load_j("cercle.json",[])
    if request.method=="POST":
        b=request.get_json() or {}; b["date"]=datetime.now().strftime("%d/%m %H:%M"); arr.append(b); save_j("cercle.json",arr); return jsonify({"ok":True})
    return jsonify(arr[::-1])
@app.route("/api/depot", methods=["GET","POST"])
def api_depot():
    arr=load_j("depots.json",[])
    if request.method=="POST":
        b=request.get_json() or {}; arr.append(b); save_j("depots.json",arr); return jsonify({"ok":True})
    return jsonify(arr[::-1])
@app.route("/manifest.json")
def manifest(): return jsonify({"name":"DROIT224","short_name":"DROIT224","start_url":"/","display":"standalone"})
if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
