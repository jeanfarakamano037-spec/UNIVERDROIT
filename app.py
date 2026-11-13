from flask import Flask, jsonify, request
import json, os, uuid, random
from datetime import datetime
app = Flask(__name__)

# ===== CONFIG GEMINI =====
def ask_gemini(question, contexte="droit guineen et OHADA"):
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        return None
    try:
        import json as js, urllib.request
        prompt = f"Tu es professeur de droit guineen, OHADA, constitutionnel, penal, civil. Reponds en francais simple, avec articles, procedure Conakry, exemples Guinee. Contexte: {contexte}. Question: {question}. Max 300 mots."
        data = js.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
        req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}", data=data, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=25) as r:
            res = js.loads(r.read())
            return res["candidates"][0]["content"]["parts"][0]["text"] + "\n\nSource: AI Gemini - Droit Guineen & OHADA"
    except Exception:
        return None

def load_j(f,d):
    if not os.path.exists(f): return d
    try: return json.load(open(f,"r",encoding="utf-8"))
    except: return d
def save_j(f,d): json.dump(d, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)

# ===== 1) COURS L1 L2 L3 - DOSSIER > PROGRAMME > CHAPITRE > SECTION > SOUS-SECTION > LECON =====
# Structure: Licence -> Matiere (dossier) -> Programme -> Chapitre -> Section -> Sous-section -> Lecon
# Tu peux ajouter 100 matieres ici, le systeme affiche auto en dossiers
COURS = {
"L1": [
 {"id":"intro_l1","matiere":"Introduction au Droit","icon":"📖","programme":[
  {"titre":"Chapitre 1: La Regle de Droit","sections":[
   {"titre":"Section 1: Definition","sous_sections":[
    {"titre":"Sous-section 1: Definition generale","lecon":"La regle de droit est generale, abstraite, obligatoire, sanctionnee par l'Etat. Elle se distingue de la morale, religion, bienseance. Droit objectif = ensemble des regles. Droits subjectifs = prerogatives. En Guinee: Constitution 22 mars 2020, lois CNT, ordonnances, coutume Malinke Manden Kalikan 1236, Peulh Pulaaku, jurisprudence Cour Supreme et CCJA Abidjan."},
    {"titre":"Sous-section 2: Caracteres","lecon":"Generale et abstraite, obligatoire, sanctionnee par l'Etat, permanente. Imperative vs supplétive. Ex: art 544 Code civil propriete."}
   ]},
   {"titre":"Section 2: Sources du droit guineen","sous_sections":[
    {"titre":"Sous-section 1: Sources nationales","lecon":"Constitution 2020 art 151 supreme, loi CNT, ordonnance President, reglement decrets arretes, coutume, jurisprudence, doctrine universites Sonfonia, Kofi Annan, UGLC."},
    {"titre":"Sous-section 2: Sources OHADA","lecon":"Traites primauté art 151, OHADA 10 Actes Uniformes primauté affaires, CEDEAO, UA, ONU."}
   ]}
  ]},
  {"titre":"Chapitre 2: Branches du Droit","sections":[
   {"titre":"Section 1: Droit Public","sous_sections":[{"titre":"Sous-section 1: Branches","lecon":"Droit constitutionnel, administratif (service public, REP 2 mois), penal (legalite), fiscal (TVA 18%), international public, finances publiques."}]},
   {"titre":"Section 2: Droit Prive","sous_sections":[{"titre":"Sous-section 1: Branches","lecon":"Droit civil (personne, famille, biens, obligations), commercial (AUDCG), travail (CDI, CDD 2 ans), international prive (conflit lois, exequatur)."}]}
  ]}
 ]},
 {"id":"const_l1","matiere":"Droit Constitutionnel","icon":"🏛️","programme":[
  {"titre":"Chapitre 1: Etat et Constitution 2020","sections":[
   {"titre":"Section 1: Etat","sous_sections":[{"titre":"Sous-section 1: Elements","lecon":"Territoire, population, pouvoir souverain. Etat unitaire decentralise Guinee vs federal USA. Etat de droit: hierarchie normes."},{"titre":"Sous-section 2: Constitution 2020 et QPC","lecon":"156 articles. President 5 ans renouvelable 1 fois. CNT 81 membres. Cour Constitutionnelle 9 membres. QPC art 95: loi contraire Constitution -> abrogation."}]}
  ]}
 ]},
 {"id":"civil_l1","matiere":"Droit Civil","icon":"⚖️","programme":[{"titre":"Chapitre 1: Personnes et Biens","sections":[{"titre":"Section 1: Personnes","sous_sections":[{"titre":"Sous-section 1: Personne physique","lecon":"Naissance vivante viable a mort. Attributs: nom, domicile, nationalite, patrimoine. Capacite 18 ans."}]}]}]},
 {"id":"histoire_l1","matiere":"Histoire du Droit","icon":"📜","programme":[{"titre":"Chapitre 1: Manden Kalikan","sections":[{"titre":"Section 1: 1236","sous_sections":[{"titre":"Sous-section 1: Charte","lecon":"Manden Kalikan 1236: premiere declaration droits humains, abolition esclavage par naissance, respect vie."}]}]}]},
],
"L2": [
 {"id":"oblig_l2","matiere":"Droit des Obligations","icon":"⚖️","programme":[{"titre":"Chapitre 1: Contrat","sections":[{"titre":"Section 1: Formation","sous_sections":[{"titre":"Sous-section 1: 4 conditions art 1128","lecon":"Consentement (erreur, dol art 1137, violence art 1140), capacite 18 ans, objet certain licite, cause licite. Nullite absolue 30 ans, relative 5 ans."}]}]}]},
 {"id":"penal_l2","matiere":"Droit Penal","icon":"🔨","programme":[{"titre":"Chapitre 1: Infraction","sections":[{"titre":"Section 1: Classification","sous_sections":[{"titre":"Sous-section 1: Crime Delit Contravention","lecon":"Crime: Cour Assises, 10 ans a perpetuite, prescription 10 ans. Delit: TPI correctionnel, 1 mois a 10 ans, 3 ans. Contravention: Simple Police, amende, 1 an. Garde a vue 48h renouvelable 96h."}]}]}]},
 {"id":"admin_l2","matiere":"Droit Administratif","icon":"🏛️","programme":[{"titre":"Chapitre 1: Acte Administratif","sections":[{"titre":"Section 1: REP","sous_sections":[{"titre":"Sous-section 1: Recours","lecon":"REP Tribunal Administratif 2 mois. Plein contentieux. Responsabilite faute simple, lourde, sans faute."}]}]}]},
 {"id":"travail_l2","matiere":"Droit du Travail","icon":"💼","programme":[{"titre":"Chapitre 1: Contrat Travail","sections":[{"titre":"Section 1: CDI CDD","sous_sections":[{"titre":"Sous-section 1: Regles","lecon":"CDI regle, CDD exception 2 ans max. Licenciement motif reel et serieux, entretien, lettre, preavis. Inspection Travail Kaloum gratuit."}]}]}]},
],
"L3": [
 {"id":"foncier_l3","matiere":"Droit Foncier","icon":"🏠","programme":[{"titre":"Chapitre 1: Titre Foncier","sections":[{"titre":"Section 1: Procedure","sous_sections":[{"titre":"Sous-section 1: 6 etapes","lecon":"1 Acte coutumier chef quartier. 2 Demande Conservation Kaloum 500k. 3 Enquete 1 mois. 4 Bornage. 5 Commission. 6 Titre 2-5M, 6-12 mois. Sans titre = occupant precaire."}]}]}]},
 {"id":"societe_l3","matiere":"Droit des Societes","icon":"🏢","programme":[{"titre":"Chapitre 1: SARL SA","sections":[{"titre":"Section 1: Creation","sous_sections":[{"titre":"Sous-section 1: SARL","lecon":"SARL 1-100 associes, capital 1M, RCCM APIP 500k, NIF, CNSS, 48h, total 1,5M. SA 10M, SAS libre."}]}]}]},
 {"id":"procedure_l3","matiere":"Procedure Civile","icon":"📋","programme":[{"titre":"Chapitre 1: TPI","sections":[{"titre":"Section 1: Procedure","sous_sections":[{"titre":"Sous-section 1: Mise en demeure","lecon":"Mise en demeure huissier 50k obligatoire art 54 CPCC, 8 jours, sinon irrecevable. Requete TPI 50k, jugement, appel 1 mois, cassation 2 mois."}]}]}]},
]
}

# ===== 2) OHADA - MEME STRUCTURE DOSSIER =====
OHADA = [
 {"id":"audcg","matiere":"AUDCG - Droit Commercial General","icon":"⚖️","programme":[{"titre":"Chapitre 1: Commercant RCCM Bail","sections":[{"titre":"Section 1: Commercant","sous_sections":[{"titre":"Sous-section 1: RCCM","lecon":"Art 2 commercant = actes commerce profession habituelle. RCCM APIP 500k, 48h. Bail commercial art 69: 2 ans min, renouvellement, indemnite eviction. Fonds commerce art 135: clientele essentielle."}]}]}]},
 {"id":"aus","matiere":"AUS - Suretes","icon":"🔒","programme":[{"titre":"Chapitre 1: Caution Hypotheque","sections":[{"titre":"Section 1: Caution","sous_sections":[{"titre":"Sous-section 1: Caution","lecon":"Art 13 caution simple (benefice discussion) ou solidaire (direct). Hypotheque art 190 immeuble, notaire, Conservation Kaloum 10 ans, rang 1er paye 1er."}]}]}]},
 {"id":"auces","matiere":"AUCE - Voies Execution","icon":"🔨","programme":[{"titre":"Chapitre 1: Saisies","sections":[{"titre":"Section 1: Saisies","sous_sections":[{"titre":"Sous-section 1: Attribution","lecon":"Art 77 saisie attribution bloque compte. Art 1 injonction payer 15j opposition. Astreinte art 33: 200k/jour. Arbitrage 36 art: 6 mois, CCJA, New York 1958."}]}]}]},
 {"id":"auscgie","matiere":"AUSCGIE - Societes","icon":"🏢","programme":[{"titre":"Chapitre 1: SARL SA","sections":[{"titre":"Section 1: Societes","sous_sections":[{"titre":"Sous-section 1: Types","lecon":"SARL 1M, SA 10M, SAS libre, SNC indéfinie, GIE. RCCM, commissaire comptes si bilan >125M."}]}]}]},
]

# ===== 3) DICTIONNAIRE A-Z + 4) TERMES - 5000 PLACES - BASE EXTENSIBLE =====
DICT = [
 {"t":"Abus de confiance","d":"Art 394 CP: Detourner chose remise a charge rendre 1-5 ans."},
 {"t":"Astreinte","d":"Art 33 AUCE: Somme par jour retard execution jugement ex 200k/jour."},
 {"t":"Avocat","d":"Inscrit Barreau Kaloum, defend TPI Cour Appel Supreme CCJA, consultation 200-500k."},
 {"t":"Bail commercial","d":"Art 69 AUDCG: 2 ans min, renouvellement, indemnite eviction."},
 {"t":"CCJA","d":"Cour Commune Justice Arbitrage Abidjan 13 juges, cassation OHADA."},
 {"t":"Dol","d":"Art 1137: Tromperie pour faire signer, annulation + dommages."},
 {"t":"Garde a vue","d":"48h renouvelable 96h, droits avocat medecin famille silence."},
 {"t":"Hypotheque","d":"Art 190 AUS: Surete immeuble, notaire, Conservation 10 ans."},
 {"t":"Injonction de payer","d":"Art 1 AUCE: Facture impayee, requete President TPI, 15j opposition."},
 {"t":"Juge","d":"Magistrat qui tranche litiges, TPI, Cour Appel, Supreme, Constitutionnelle."},
 {"t":"Jurisprudence","d":"Decisions Cours Tribunaux qui font reference."},
 {"t":"Nullite","d":"Absolue 30 ans, relative 5 ans, retroactif."},
 {"t":"OHADA","d":"17 pays, 10 Actes Uniformes, CCJA Abidjan."},
 {"t":"QPC","d":"Question Prioritaire Constitutionnalite, loi contraire Constitution -> abrogation."},
 {"t":"RCCM","d":"Registre Commerce APIP 500k obligatoire commercant."},
 {"t":"SARL","d":"1-100 associes, capital 1M, responsabilite limitee."},
 {"t":"Titre Foncier","d":"Seul papier propriete terrain Guinee, Conservation Kaloum, 2-5M."},
]
# Pour atteindre 5000: l'app charge aussi dict.json si tu le deposes, et Gemini complete
DICT += load_j("dict_extra.json", [])

TERMES = load_j("termes.json", [{"t":"Acte authentique","d":"Acte notaire force executoire."},{"t":"Acte sous seing prive","d":"Acte signe parties sans notaire."}])

# ===== 5) QUIZ - 5000 PLACES - BADGE APRES 20 QUESTIONS =====
QUIZ = {
"L1": [{"q":"Constitution 2020 Guinee = quelle Republique?","o":["3e","4e","5e"],"r":1,"e":"4e Republique 2020"},{"q":"Garde a vue max?","o":["24h","48h renouvelable 96h","7j"],"r":1,"e":"48h x2 = 96h"},{"q":"OHADA pays?","o":["10","17","54"],"r":1,"e":"17 pays"},{"q":"Sans mise en demeure TPI?","o":["Irrecevable","OK","Amende"],"r":0,"e":"Art 54 CPCC obligatoire"}],
"L2": [{"q":"Crime juge par?","o":["TPI","Cour Assises","Supreme"],"r":1,"e":"Assises jury"},{"q":"SARL capital min?","o":["100k","1M","10M"],"r":1,"e":"1M OHADA"},{"q":"CCJA ou?","o":["Conakry","Abidjan","Dakar"],"r":1,"e":"Abidjan"}],
"L3": [{"q":"Titre Foncier ou?","o":["Mairie","Conservation Kaloum","APIP"],"r":1,"e":"Conservation Kaloum"},{"q":"Hypotheque rang?","o":["Derniere 1ere","Premiere 1ere","Pas rang"],"r":1,"e":"Premiere inscrite payee 1ere"}],
"OHADA": [{"q":"OHADA = ?","o":["Harmonisation Droit Affaires","Humanitaire","Douane"],"r":0,"e":"Harmonisation Droit Affaires Afrique"}]
}
QUIZ.update(load_j("quiz_extra.json", {}))

FAQ_BASE = [("juge","Juge = magistrat qui tranche litiges, TPI, Cour Appel, Supreme. Recrutement concours ENAM, salaire 3-5M."),("avocat","Avocat = Barreau Kaloum, defend clients, consultation 200-500k, TPI 2-5M."),("sarl","SARL: APIP 1,5M 48h, capital 1M, RCCM 500k, NIF, CNSS."),("terrain","Titre Foncier seul papier propriete. Conservation Kaloum 2-5M 6-12 mois. Verifier livre foncier avant payer.")]

def moteur_faq(q):
    rep = ask_gemini(q)
    if rep: return rep
    ql=q.lower()
    for k,a in FAQ_BASE:
        if k in ql: return a
    return f"Pour '{q}': Dis-moi plus: civil, penal, commerce OHADA, travail, foncier? Ex: 'c'est qui le juge?' 'comment creer SARL?'"

@app.route("/")
def home():
    return """<!DOCTYPE html><html><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>DROIT224 - Universite Droit</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#050510;color:#fff;font-family:Arial}.header{text-align:center;padding:14px;background:#0a0a2a;border-bottom:3px solid #f9c00f;position:sticky;top:0;z-index:30}.tabs{display:flex;gap:4px;padding:6px;background:#0a0a1a;overflow-x:auto;position:sticky;top:95px;z-index:20}.tabs button{padding:8px 11px;border-radius:18px;border:1px solid #222;background:#151530;color:#aaa;font-size:10px;font-weight:800;white-space:nowrap}.tabs button.active{background:#f9c00f;color:#000}.view{display:none;padding:10px}.view.active{display:block}.card{background:#10102a;border:1px solid #1a1a3a;border-radius:12px;padding:12px;margin:8px 0;cursor:pointer}.card:hover{border-color:#f9c00f}.badge{padding:3px 8px;border-radius:12px;font-size:9px;font-weight:900;color:#000;background:#f9c00f}input,select,textarea{width:100%;padding:9px;margin:4px 0;border-radius:8px;border:1px solid #222;background:#111;color:#fff} .btn{padding:9px 14px;border-radius:18px;border:none;font-weight:800;background:#f9c00f;color:#000;cursor:pointer}.small{font-size:13px;color:#ddd;line-height:1.7;white-space:pre-wrap}.lecon{background:#0a1a0a;border:2px solid #76ff03;padding:14px;border-radius:10px;margin-top:10px}.licence-card{background:linear-gradient(135deg,#1a1a4a,#0a0a2a);border:2px solid #f9c00f;padding:18px;border-radius:16px;margin:10px 0;text-align:center;cursor:pointer}</style></head><body>
<div class="header"><h1 style="color:#f9c00f;font-size:28px">DROIT224</h1><p style="font-size:9px;color:#aaa">UNIVERSITE DROIT • L1 L2 L3 • OHADA • DICTIONNAIRE • QUIZ • FAQ AI • DOSSIER • CERCLE</p><button class="btn" onclick="downloadApp()" style="margin-top:8px">📥 TELECHARGER L'APP</button></div>
<div class="tabs"><button class="active" onclick="show('cours')">📚 COURS</button><button onclick="show('ohada')">⚖️ OHADA</button><button onclick="show('dict')">📖 DICTIONNAIRE</button><button onclick="show('quiz')">🏆 QUIZ</button><button onclick="show('faq')">🤖 FAQ AI</button><button onclick="show('dossier')">📂 DOSSIER JUSTICE</button><button onclick="show('cercle')">💬 CERCLE</button><button onclick="show('depot')">📤 DEPOT COURS</button></div>

<div id="cours" class="view active"><h2>📚 COURS - Choisis ta Licence</h2><div id="licences"></div><div id="matieres"></div><div id="detail"></div></div>
<div id="ohada" class="view"><h2>⚖️ OHADA</h2><div id="ohadaList"></div><div id="ohadaDetail"></div></div>
<div id="dict" class="view"><h2>📖 Dictionnaire A-Z + Termes Juridiques</h2><input id="searchDict" placeholder="Cherche un mot: ex juge, SARL, hypotheque..." oninput="filterDict()"><div id="dictList"></div></div>
<div id="quiz" class="view"><h2>🏆 QUIZ - Badge apres 20 questions</h2><select id="quizLic"><option>L1</option><option>L2</option><option>L3</option><option>OHADA</option></select><button class="btn" onclick="startQuiz()">Commencer Quiz</button><div id="quizBox"></div></div>
<div id="faq" class="view"><h2>🤖 FAQ AI - Pose ta question droit</h2><input id="faqQ" placeholder="Ex: c'est qui le juge? Comment creer SARL?"><button class="btn" onclick="askFaq()">Demander a AI</button><div id="faqAns" class="small"></div></div>
<div id="dossier" class="view"><h2>📂 DOSSIER JUSTICE - Decris ton cas</h2><input id="dNom" placeholder="Ton nom"><select id="dRang"><option>Etudiant</option><option>Prof</option><option>Enseignant</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option><option>Citoyen</option></select><select id="dType"><option>Licenciement</option><option>Dette</option><option>Terre Foncier</option><option>Divorce</option><option>Vol</option><option>Viol</option><option>Contrat</option><option>Crime</option><option>Succession</option><option>Autre</option></select><textarea id="dCas" placeholder="Decris ton cas: qui, quoi, ou, quand..."></textarea><button class="btn" onclick="submitDossier()">Soumettre Dossier</button><div id="dossierList"></div></div>
<div id="cercle" class="view"><h2>💬 CERCLE - Conversation Droit</h2><input id="cNom" placeholder="Ton nom"><select id="cRang"><option>Etudiant</option><option>Prof</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option></select><textarea id="cMsg" placeholder="Parle droit ici..."></textarea><button class="btn" onclick="sendCercle()">Envoyer</button><div id="cercleList"></div></div>
<div id="depot" class="view"><h2>📤 DEPOT COURS PDF - Tout le monde peut deposer</h2><input id="pNom" placeholder="Ton nom"><select id="pRang"><option>Prof</option><option>Enseignant</option><option>Docteur</option><option>Juriste</option><option>Juge</option><option>Avocat</option><option>Procureur</option><option>Etudiant</option></select><input id="pTitre" placeholder="Titre du cours"><input id="pLic" placeholder="Licence: L1 / L2 / L3 / OHADA"><textarea id="pDesc" placeholder="Description du cours..."></textarea><button class="btn" onclick="submitDepot()">Deposer Cours</button><div id="depotList"></div></div>

<script>
let COURS={}, OHADA=[], DICT=[], QUIZ={};
function show(id){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));document.getElementById(id).classList.add('active');document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'))}
async function load(){let r=await fetch('/api/data');let d=await r.json();COURS=d.cours;OHADA=d.ohada;DICT=d.dict;QUIZ=d.quiz;renderLic();renderOhada();renderDict();loadDossiers();loadCercle();loadDepot()}
function renderLic(){let h='';for(let lic in COURS){h+=`<div class="licence-card" onclick="showMat('${lic}')"><h2>🎓 LICENCE ${lic}</h2><p>${COURS[lic].length} matieres</p></div>`}document.getElementById('licences').innerHTML=h}
function showMat(lic){let h=`<h3>Licence ${lic}</h3>`;COURS[lic].forEach((m,i)=>{h+=`<div class="card" onclick="showProg('${lic}',${i})">📂 ${m.icon} ${m.matiere} <span class="badge">${m.programme.length} chapitres</span></div>`});document.getElementById('matieres').innerHTML=h;document.getElementById('detail').innerHTML=''}
function showProg(lic,mi){let m=COURS[lic][mi];let h=`<h3>📂 ${m.matiere}</h3>`;m.programme.forEach(ch=>{h+=`<div class="card"><b>${ch.titre}</b>`;ch.sections.forEach(s=>{h+=`<p>📁 ${s.titre}</p>`;s.sous_sections.forEach(ss=>{h+=`<div style="margin-left:12px"><b>📄 ${ss.titre}</b><div class="lecon small">${ss.lecon}</div></div>`})});h+=`</div>`});document.getElementById('detail').innerHTML=h}
function renderOhada(){let h='';OHADA.forEach((m,i)=>{h+=`<div class="card" onclick="showOhada(${i})">📂 ${m.icon} ${m.matiere}</div>`});document.getElementById('ohadaList').innerHTML=h}
function showOhada(i){let m=OHADA[i];let h=`<h3>${m.matiere}</h3>`;m.programme.forEach(ch=>{h+=`<div class="card"><b>${ch.titre}</b>`;ch.sections.forEach(s=>{h+=`<p>${s.titre}</p>`;s.sous_sections.forEach(ss=>{h+=`<div class="lecon small"><b>${ss.titre}</b><br>${ss.lecon}</div>`})});h+=`</div>`});document.getElementById('ohadaDetail').innerHTML=h}
function renderDict(){let h='';DICT.forEach(d=>{h+=`<div class="card"><b>${d.t}</b><div class="small">${d.d}</div></div>`});document.getElementById('dictList').innerHTML=h}
function filterDict(){let q=document.getElementById('searchDict').value.toLowerCase();let f=DICT.filter(d=>d.t.toLowerCase().includes(q));document.getElementById('dictList').innerHTML=f.map(d=>`<div class="card"><b>${d.t}</b><div class="small">${d.d}</div></div>`).join('')}
let qi=0,score=0,cur=[];
function startQuiz(){let lic=document.getElementById('quizLic').value;cur=QUIZ[lic]||[];qi=0;score=0;showQ()}
function showQ(){if(qi>=cur.length){let badge=score>=3?'🏆 BADGE OR - EXPERT DROIT':score>=1?'🥈 BADGE ARGENT':'📜 Continue';document.getElementById('quizBox').innerHTML=`<h3>Score: ${score}/${cur.length}</h3><div>${badge}</div><p>Apres 20 questions, tu gagnes Badge Or!</p>`;return}let q=cur[qi];document.getElementById('quizBox').innerHTML=`<div class="card"><b>Q${qi+1}: ${q.q}</b>${q.o.map((o,i)=>`<button class="btn" style="display:block;margin:4px" onclick="ans(${i})">${o}</button>`).join('')}</div>`}
function ans(i){if(i==cur[qi].r)score++;alert(cur[qi].e);qi++;showQ()}
async function askFaq(){let q=document.getElementById('faqQ').value;let r=await fetch('/api/faq?q='+encodeURIComponent(q));let d=await r.json();document.getElementById('faqAns').innerText=d.answer}
async function submitDossier(){let b={nom:document.getElementById('dNom').value,rang:document.getElementById('dRang').value,type:document.getElementById('dType').value,cas:document.getElementById('dCas').value};await fetch('/api/dossier',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadDossiers()}
async function loadDossiers(){let r=await fetch('/api/dossier');let d=await r.json();document.getElementById('dossierList').innerHTML=d.map(x=>`<div class="card"><b>${x.type} - ${x.nom} (${x.rang})</b><div class="small">${x.cas}</div><div>${(x.aides||[]).map(a=>`<p>💬 ${a.nom} (${a.rang}): ${a.msg}</p>`).join('')}</div><input id="aide-${x.id}" placeholder="Aider: ton avis..."><button class="btn" onclick="aider('${x.id}')">Aider</button></div>`).join('')}
async function aider(id){let msg=document.getElementById('aide-'+id).value;let nom=document.getElementById('dNom').value||'Anonyme';let rang=document.getElementById('dRang').value;await fetch('/api/dossier/aide',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id,nom,rang,msg})});loadDossiers()}
async function sendCercle(){let b={nom:document.getElementById('cNom').value,rang:document.getElementById('cRang').value,msg:document.getElementById('cMsg').value};await fetch('/api/cercle',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadCercle()}
async function loadCercle(){let r=await fetch('/api/cercle');let d=await r.json();document.getElementById('cercleList').innerHTML=d.map(x=>`<div class="card"><b>${x.nom} (${x.rang})</b><div class="small">${x.msg}</div><small>${x.date||''}</small></div>`).join('')}
async function submitDepot(){let b={nom:document.getElementById('pNom').value,rang:document.getElementById('pRang').value,titre:document.getElementById('pTitre').value,lic:document.getElementById('pLic').value,desc:document.getElementById('pDesc').value};await fetch('/api/depot',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(b)});loadDepot()}
async function loadDepot(){let r=await fetch('/api/depot');let d=await r.json();document.getElementById('depotList').innerHTML=d.map(x=>`<div class="card"><b>📄 ${x.titre} - ${x.lic}</b><div class="small">Par ${x.nom} (${x.rang}) - ${x.desc}</div></div>`).join('')}
function downloadApp(){alert('Pour telecharger: Chrome -> Menu -> Ajouter a ecran accueil. Ton app devient comme Play Store!')}
load()
</script></body></html>
"""

@app.route("/api/data")
def api_data(): return jsonify({"cours":COURS,"ohada":OHADA,"dict":DICT,"quiz":QUIZ,"termes":TERMES})
@app.route("/api/faq")
def api_faq():
    q=request.args.get("q","")
    return jsonify({"answer": moteur_faq(q)})
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
