"""
Université Droit — Tout le Droit
Application Flask prête pour Render et GitHub.

Lancement local :   python app.py
Lancement Render :  gunicorn app:app
"""
import os

from flask import Flask, Response

app = Flask(__name__)

HTML_PAGE = r'''<!DOCTYPE html>
<html lang="en">
<head><style>
@font-face {
  font-family: "Optimistic";
  font-style: normal;
  font-weight: 400 600;
  font-display: swap;
  src: url("/fonts/OptimisticAI_VF_Optimized.woff2") format("woff2");
}
@font-face {
  font-family: "Optimistic Mono";
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url("/fonts/OptimisticMono_W_TextRegular.woff2") format("woff2");
}
:where(html) {
  font-family: "Optimistic", system-ui, sans-serif;
}
:where(code, pre, kbd, samp) {
  font-family: "Optimistic Mono", ui-monospace, monospace;
}
</style>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>React Artifact</title>
  <script>(function installDevicePermissionRuntime() {
  if (window.parent === window)
    return;
  let parentOrigin;
  try {
    const embeddingOrigin = window.location.ancestorOrigins?.[0] || document.referrer, { hostname, origin, port, protocol } = new URL(embeddingOrigin), supportedHost = hostname === "meta.ai" || hostname === "ecto1.ai" || [".meta.ai", ".ecto1.ai", ".internalfb.com", ".hatch.club"].some((suffix) => hostname.endsWith(suffix));
    if (hostname === "localhost" && (protocol === "http:" || protocol === "https:") || protocol === "https:" && port === "" && supportedHost)
      parentOrigin = origin;
  } catch {
    return;
  }
  if (!parentOrigin)
    return;
  function request(capability) {
    try {
      const policy = document.permissionsPolicy || document.featurePolicy;
      if (navigator.userActivation?.isActive === !0 && policy?.allowsFeature(capability) === !1)
        window.parent.postMessage({ type: "ecto:artifact-device-permission-request", version: 1, capability }, parentOrigin);
    } catch {}
  }
  function hasAudio(constraints) {
    for (let value = constraints;value != null; value = Object.getPrototypeOf(value)) {
      const descriptor = Object.getOwnPropertyDescriptor(value, "audio");
      if (descriptor)
        return Boolean(descriptor.value);
    }
    return !1;
  }
  function wrap(receiver, name, capability, enabled) {
    try {
      if ((document.permissionsPolicy || document.featurePolicy)?.allowsFeature(capability) !== !1)
        return;
      const native = receiver?.[name];
      if (typeof native !== "function")
        return;
      receiver[name] = function() {
        try {
          if (this === receiver && enabled(arguments))
            request(capability);
        } catch {}
        return Reflect.apply(native, this, arguments);
      };
    } catch {}
  }
  wrap(navigator.mediaDevices, "getUserMedia", "microphone", (args) => hasAudio(args[0]));
  const hasPositionCallback = (args) => typeof args[0] === "function";
  wrap(navigator.geolocation, "getCurrentPosition", "geolocation", hasPositionCallback);
  wrap(navigator.geolocation, "watchPosition", "geolocation", hasPositionCallback);
})();</script>
  <style>*, ::before, ::after {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
  --tw-contain-size:  ;
  --tw-contain-layout:  ;
  --tw-contain-paint:  ;
  --tw-contain-style:  ;
}

::backdrop {
  --tw-border-spacing-x: 0;
  --tw-border-spacing-y: 0;
  --tw-translate-x: 0;
  --tw-translate-y: 0;
  --tw-rotate: 0;
  --tw-skew-x: 0;
  --tw-skew-y: 0;
  --tw-scale-x: 1;
  --tw-scale-y: 1;
  --tw-pan-x:  ;
  --tw-pan-y:  ;
  --tw-pinch-zoom:  ;
  --tw-scroll-snap-strictness: proximity;
  --tw-gradient-from-position:  ;
  --tw-gradient-via-position:  ;
  --tw-gradient-to-position:  ;
  --tw-ordinal:  ;
  --tw-slashed-zero:  ;
  --tw-numeric-figure:  ;
  --tw-numeric-spacing:  ;
  --tw-numeric-fraction:  ;
  --tw-ring-inset:  ;
  --tw-ring-offset-width: 0px;
  --tw-ring-offset-color: #fff;
  --tw-ring-color: rgb(59 130 246 / 0.5);
  --tw-ring-offset-shadow: 0 0 #0000;
  --tw-ring-shadow: 0 0 #0000;
  --tw-shadow: 0 0 #0000;
  --tw-shadow-colored: 0 0 #0000;
  --tw-blur:  ;
  --tw-brightness:  ;
  --tw-contrast:  ;
  --tw-grayscale:  ;
  --tw-hue-rotate:  ;
  --tw-invert:  ;
  --tw-saturate:  ;
  --tw-sepia:  ;
  --tw-drop-shadow:  ;
  --tw-backdrop-blur:  ;
  --tw-backdrop-brightness:  ;
  --tw-backdrop-contrast:  ;
  --tw-backdrop-grayscale:  ;
  --tw-backdrop-hue-rotate:  ;
  --tw-backdrop-invert:  ;
  --tw-backdrop-opacity:  ;
  --tw-backdrop-saturate:  ;
  --tw-backdrop-sepia:  ;
  --tw-contain-size:  ;
  --tw-contain-layout:  ;
  --tw-contain-paint:  ;
  --tw-contain-style:  ;
}

/*
! tailwindcss v3.4.18 | MIT License | https://tailwindcss.com
*/

/*
1. Prevent padding and border from affecting element width. (https://github.com/mozdevs/cssremedy/issues/4)
2. Allow adding a border to an element by just adding a border-width. (https://github.com/tailwindcss/tailwindcss/pull/116)
*/

*,
::before,
::after {
  box-sizing: border-box;
  /* 1 */
  border-width: 0;
  /* 2 */
  border-style: solid;
  /* 2 */
  border-color: #e5e7eb;
  /* 2 */
}

::before,
::after {
  --tw-content: '';
}

/*
1. Use a consistent sensible line-height in all browsers.
2. Prevent adjustments of font size after orientation changes in iOS.
3. Use a more readable tab size.
4. Use the user's configured `sans` font-family by default.
5. Use the user's configured `sans` font-feature-settings by default.
6. Use the user's configured `sans` font-variation-settings by default.
7. Disable tap highlights on iOS
*/

html,
:host {
  line-height: 1.5;
  /* 1 */
  -webkit-text-size-adjust: 100%;
  /* 2 */
  -moz-tab-size: 4;
  /* 3 */
  -o-tab-size: 4;
     tab-size: 4;
  /* 3 */
  font-family: ui-sans-serif, system-ui, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
  /* 4 */
  font-feature-settings: normal;
  /* 5 */
  font-variation-settings: normal;
  /* 6 */
  -webkit-tap-highlight-color: transparent;
  /* 7 */
}

/*
1. Remove the margin in all browsers.
2. Inherit line-height from `html` so users can set them as a class directly on the `html` element.
*/

body {
  margin: 0;
  /* 1 */
  line-height: inherit;
  /* 2 */
}

/*
1. Add the correct height in Firefox.
2. Correct the inheritance of border color in Firefox. (https://bugzilla.mozilla.org/show_bug.cgi?id=190655)
3. Ensure horizontal rules are visible by default.
*/

hr {
  height: 0;
  /* 1 */
  color: inherit;
  /* 2 */
  border-top-width: 1px;
  /* 3 */
}

/*
Add the correct text decoration in Chrome, Edge, and Safari.
*/

abbr:where([title]) {
  -webkit-text-decoration: underline dotted;
          text-decoration: underline dotted;
}

/*
Remove the default font size and weight for headings.
*/

h1,
h2,
h3,
h4,
h5,
h6 {
  font-size: inherit;
  font-weight: inherit;
}

/*
Reset links to optimize for opt-in styling instead of opt-out.
*/

a {
  color: inherit;
  text-decoration: inherit;
}

/*
Add the correct font weight in Edge and Safari.
*/

b,
strong {
  font-weight: bolder;
}

/*
1. Use the user's configured `mono` font-family by default.
2. Use the user's configured `mono` font-feature-settings by default.
3. Use the user's configured `mono` font-variation-settings by default.
4. Correct the odd `em` font sizing in all browsers.
*/

code,
kbd,
samp,
pre {
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
  /* 1 */
  font-feature-settings: normal;
  /* 2 */
  font-variation-settings: normal;
  /* 3 */
  font-size: 1em;
  /* 4 */
}

/*
Add the correct font size in all browsers.
*/

small {
  font-size: 80%;
}

/*
Prevent `sub` and `sup` elements from affecting the line height in all browsers.
*/

sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

sub {
  bottom: -0.25em;
}

sup {
  top: -0.5em;
}

/*
1. Remove text indentation from table contents in Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=999088, https://bugs.webkit.org/show_bug.cgi?id=201297)
2. Correct table border color inheritance in all Chrome and Safari. (https://bugs.chromium.org/p/chromium/issues/detail?id=935729, https://bugs.webkit.org/show_bug.cgi?id=195016)
3. Remove gaps between table borders by default.
*/

table {
  text-indent: 0;
  /* 1 */
  border-color: inherit;
  /* 2 */
  border-collapse: collapse;
  /* 3 */
}

/*
1. Change the font styles in all browsers.
2. Remove the margin in Firefox and Safari.
3. Remove default padding in all browsers.
*/

button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  /* 1 */
  font-feature-settings: inherit;
  /* 1 */
  font-variation-settings: inherit;
  /* 1 */
  font-size: 100%;
  /* 1 */
  font-weight: inherit;
  /* 1 */
  line-height: inherit;
  /* 1 */
  letter-spacing: inherit;
  /* 1 */
  color: inherit;
  /* 1 */
  margin: 0;
  /* 2 */
  padding: 0;
  /* 3 */
}

/*
Remove the inheritance of text transform in Edge and Firefox.
*/

button,
select {
  text-transform: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Remove default button styles.
*/

button,
input:where([type='button']),
input:where([type='reset']),
input:where([type='submit']) {
  -webkit-appearance: button;
  /* 1 */
  background-color: transparent;
  /* 2 */
  background-image: none;
  /* 2 */
}

/*
Use the modern Firefox focus style for all focusable elements.
*/

:-moz-focusring {
  outline: auto;
}

/*
Remove the additional `:invalid` styles in Firefox. (https://github.com/mozilla/gecko-dev/blob/2f9eacd9d3d995c937b4251a5557d95d494c9be1/layout/style/res/forms.css#L728-L737)
*/

:-moz-ui-invalid {
  box-shadow: none;
}

/*
Add the correct vertical alignment in Chrome and Firefox.
*/

progress {
  vertical-align: baseline;
}

/*
Correct the cursor style of increment and decrement buttons in Safari.
*/

::-webkit-inner-spin-button,
::-webkit-outer-spin-button {
  height: auto;
}

/*
1. Correct the odd appearance in Chrome and Safari.
2. Correct the outline style in Safari.
*/

[type='search'] {
  -webkit-appearance: textfield;
  /* 1 */
  outline-offset: -2px;
  /* 2 */
}

/*
Remove the inner padding in Chrome and Safari on macOS.
*/

::-webkit-search-decoration {
  -webkit-appearance: none;
}

/*
1. Correct the inability to style clickable types in iOS and Safari.
2. Change font properties to `inherit` in Safari.
*/

::-webkit-file-upload-button {
  -webkit-appearance: button;
  /* 1 */
  font: inherit;
  /* 2 */
}

/*
Add the correct display in Chrome and Safari.
*/

summary {
  display: list-item;
}

/*
Removes the default spacing and border for appropriate elements.
*/

blockquote,
dl,
dd,
h1,
h2,
h3,
h4,
h5,
h6,
hr,
figure,
p,
pre {
  margin: 0;
}

fieldset {
  margin: 0;
  padding: 0;
}

legend {
  padding: 0;
}

ol,
ul,
menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

/*
Reset default styling for dialogs.
*/

dialog {
  padding: 0;
}

/*
Prevent resizing textareas horizontally by default.
*/

textarea {
  resize: vertical;
}

/*
1. Reset the default placeholder opacity in Firefox. (https://github.com/tailwindlabs/tailwindcss/issues/3300)
2. Set the default placeholder color to the user's configured gray 400 color.
*/

input::-moz-placeholder, textarea::-moz-placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

input::placeholder,
textarea::placeholder {
  opacity: 1;
  /* 1 */
  color: #9ca3af;
  /* 2 */
}

/*
Set the default cursor for buttons.
*/

button,
[role="button"] {
  cursor: pointer;
}

/*
Make sure disabled buttons don't get the pointer cursor.
*/

:disabled {
  cursor: default;
}

/*
1. Make replaced elements `display: block` by default. (https://github.com/mozdevs/cssremedy/issues/14)
2. Add `vertical-align: middle` to align replaced elements more sensibly by default. (https://github.com/jensimmons/cssremedy/issues/14#issuecomment-634934210)
   This can trigger a poorly considered lint error in some tools but is included by design.
*/

img,
svg,
video,
canvas,
audio,
iframe,
embed,
object {
  display: block;
  /* 1 */
  vertical-align: middle;
  /* 2 */
}

/*
Constrain images and videos to the parent width and preserve their intrinsic aspect ratio. (https://github.com/mozdevs/cssremedy/issues/14)
*/

img,
video {
  max-width: 100%;
  height: auto;
}

/* Make elements with the HTML hidden attribute stay hidden by default */

[hidden]:where(:not([hidden="until-found"])) {
  display: none;
}

.pointer-events-none {
  pointer-events: none;
}

.visible {
  visibility: visible;
}

.fixed {
  position: fixed;
}

.absolute {
  position: absolute;
}

.relative {
  position: relative;
}

.sticky {
  position: sticky;
}

.inset-0 {
  inset: 0px;
}

.bottom-0 {
  bottom: 0px;
}

.left-0 {
  left: 0px;
}

.left-3 {
  left: 0.75rem;
}

.left-7 {
  left: 1.75rem;
}

.right-0 {
  right: 0px;
}

.right-4 {
  right: 1rem;
}

.top-24 {
  top: 6rem;
}

.top-3 {
  top: 0.75rem;
}

.top-4 {
  top: 1rem;
}

.z-40 {
  z-index: 40;
}

.z-50 {
  z-index: 50;
}

.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

.mb-3 {
  margin-bottom: 0.75rem;
}

.ml-2 {
  margin-left: 0.5rem;
}

.ml-4 {
  margin-left: 1rem;
}

.ml-auto {
  margin-left: auto;
}

.mr-2 {
  margin-right: 0.5rem;
}

.mt-1 {
  margin-top: 0.25rem;
}

.mt-2 {
  margin-top: 0.5rem;
}

.mt-3 {
  margin-top: 0.75rem;
}

.mt-4 {
  margin-top: 1rem;
}

.mt-5 {
  margin-top: 1.25rem;
}

.mt-6 {
  margin-top: 1.5rem;
}

.mt-7 {
  margin-top: 1.75rem;
}

.line-clamp-2 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 2;
}

.line-clamp-3 {
  overflow: hidden;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
}

.block {
  display: block;
}

.inline {
  display: inline;
}

.flex {
  display: flex;
}

.inline-flex {
  display: inline-flex;
}

.grid {
  display: grid;
}

.hidden {
  display: none;
}

.h-10 {
  height: 2.5rem;
}

.h-11 {
  height: 2.75rem;
}

.h-2 {
  height: 0.5rem;
}

.h-3 {
  height: 0.75rem;
}

.h-4 {
  height: 1rem;
}

.h-44 {
  height: 11rem;
}

.h-5 {
  height: 1.25rem;
}

.h-8 {
  height: 2rem;
}

.h-9 {
  height: 2.25rem;
}

.h-full {
  height: 100%;
}

.h-px {
  height: 1px;
}

.max-h-\[420px\] {
  max-height: 420px;
}

.max-h-\[520px\] {
  max-height: 520px;
}

.min-h-\[110px\] {
  min-height: 110px;
}

.min-h-\[140px\] {
  min-height: 140px;
}

.min-h-\[280px\] {
  min-height: 280px;
}

.min-h-\[300px\] {
  min-height: 300px;
}

.min-h-screen {
  min-height: 100vh;
}

.w-10 {
  width: 2.5rem;
}

.w-11 {
  width: 2.75rem;
}

.w-3 {
  width: 0.75rem;
}

.w-4 {
  width: 1rem;
}

.w-44 {
  width: 11rem;
}

.w-5 {
  width: 1.25rem;
}

.w-8 {
  width: 2rem;
}

.w-9 {
  width: 2.25rem;
}

.w-fit {
  width: -moz-fit-content;
  width: fit-content;
}

.w-full {
  width: 100%;
}

.min-w-0 {
  min-width: 0px;
}

.min-w-\[68px\] {
  min-width: 68px;
}

.max-w-2xl {
  max-width: 42rem;
}

.max-w-7xl {
  max-width: 80rem;
}

.max-w-\[88\%\] {
  max-width: 88%;
}

.max-w-lg {
  max-width: 32rem;
}

.max-w-md {
  max-width: 28rem;
}

.max-w-xl {
  max-width: 36rem;
}

.flex-1 {
  flex: 1 1 0%;
}

.shrink-0 {
  flex-shrink: 0;
}

.cursor-pointer {
  cursor: pointer;
}

.select-none {
  -webkit-user-select: none;
     -moz-user-select: none;
          user-select: none;
}

.grid-cols-2 {
  grid-template-columns: repeat(2, minmax(0, 1fr));
}

.grid-cols-3 {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.grid-cols-5 {
  grid-template-columns: repeat(5, minmax(0, 1fr));
}

.flex-col {
  flex-direction: column;
}

.flex-wrap {
  flex-wrap: wrap;
}

.place-items-end {
  place-items: end;
}

.place-items-center {
  place-items: center;
}

.items-start {
  align-items: flex-start;
}

.items-end {
  align-items: flex-end;
}

.items-center {
  align-items: center;
}

.justify-center {
  justify-content: center;
}

.justify-between {
  justify-content: space-between;
}

.gap-0\.5 {
  gap: 0.125rem;
}

.gap-1 {
  gap: 0.25rem;
}

.gap-1\.5 {
  gap: 0.375rem;
}

.gap-2 {
  gap: 0.5rem;
}

.gap-3 {
  gap: 0.75rem;
}

.gap-4 {
  gap: 1rem;
}

.space-y-1 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.25rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.25rem * var(--tw-space-y-reverse));
}

.space-y-2 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));
}

.space-y-3 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(0.75rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(0.75rem * var(--tw-space-y-reverse));
}

.space-y-4 > :not([hidden]) ~ :not([hidden]) {
  --tw-space-y-reverse: 0;
  margin-top: calc(1rem * calc(1 - var(--tw-space-y-reverse)));
  margin-bottom: calc(1rem * var(--tw-space-y-reverse));
}

.overflow-auto {
  overflow: auto;
}

.overflow-hidden {
  overflow: hidden;
}

.overflow-x-auto {
  overflow-x: auto;
}

.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.whitespace-pre-line {
  white-space: pre-line;
}

.rounded-2xl {
  border-radius: 1rem;
}

.rounded-3xl {
  border-radius: 1.5rem;
}

.rounded-\[28px\] {
  border-radius: 28px;
}

.rounded-\[2px\] {
  border-radius: 2px;
}

.rounded-full {
  border-radius: 9999px;
}

.rounded-lg {
  border-radius: 0.5rem;
}

.rounded-xl {
  border-radius: 0.75rem;
}

.rounded-br-sm {
  border-bottom-right-radius: 0.125rem;
}

.rounded-tl-sm {
  border-top-left-radius: 0.125rem;
}

.border {
  border-width: 1px;
}

.border-b {
  border-bottom-width: 1px;
}

.border-t {
  border-top-width: 1px;
}

.border-dashed {
  border-style: dashed;
}

.\!border-white\/20 {
  border-color: rgb(255 255 255 / 0.2) !important;
}

.\!border-white\/30 {
  border-color: rgb(255 255 255 / 0.3) !important;
}

.border-\[var\(--line\)\] {
  border-color: var(--line);
}

.border-amber-200 {
  --tw-border-opacity: 1;
  border-color: rgb(253 230 138 / var(--tw-border-opacity, 1));
}

.border-emerald-300 {
  --tw-border-opacity: 1;
  border-color: rgb(110 231 183 / var(--tw-border-opacity, 1));
}

.border-rose-300 {
  --tw-border-opacity: 1;
  border-color: rgb(253 164 175 / var(--tw-border-opacity, 1));
}

.border-white\/10 {
  border-color: rgb(255 255 255 / 0.1);
}

.border-white\/20 {
  border-color: rgb(255 255 255 / 0.2);
}

.\!bg-\[\#071631\] {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(7 22 49 / var(--tw-bg-opacity, 1)) !important;
}

.\!bg-\[\#f4e3b0\] {
  --tw-bg-opacity: 1 !important;
  background-color: rgb(244 227 176 / var(--tw-bg-opacity, 1)) !important;
}

.\!bg-white\/10 {
  background-color: rgb(255 255 255 / 0.1) !important;
}

.bg-\[\#071631\] {
  --tw-bg-opacity: 1;
  background-color: rgb(7 22 49 / var(--tw-bg-opacity, 1));
}

.bg-\[\#c9a24b\] {
  --tw-bg-opacity: 1;
  background-color: rgb(201 162 75 / var(--tw-bg-opacity, 1));
}

.bg-\[\#e7c87a\] {
  --tw-bg-opacity: 1;
  background-color: rgb(231 200 122 / var(--tw-bg-opacity, 1));
}

.bg-\[\#f4e3b0\] {
  --tw-bg-opacity: 1;
  background-color: rgb(244 227 176 / var(--tw-bg-opacity, 1));
}

.bg-\[var\(--paper\)\] {
  background-color: var(--paper);
}

.bg-\[var\(--surface\)\] {
  background-color: var(--surface);
}

.bg-amber-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 251 235 / var(--tw-bg-opacity, 1));
}

.bg-black\/60 {
  background-color: rgb(0 0 0 / 0.6);
}

.bg-emerald-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(236 253 245 / var(--tw-bg-opacity, 1));
}

.bg-rose-50 {
  --tw-bg-opacity: 1;
  background-color: rgb(255 241 242 / var(--tw-bg-opacity, 1));
}

.bg-white {
  --tw-bg-opacity: 1;
  background-color: rgb(255 255 255 / var(--tw-bg-opacity, 1));
}

.bg-white\/10 {
  background-color: rgb(255 255 255 / 0.1);
}

.bg-white\/20 {
  background-color: rgb(255 255 255 / 0.2);
}

.\!p-2 {
  padding: 0.5rem !important;
}

.p-2 {
  padding: 0.5rem;
}

.p-2\.5 {
  padding: 0.625rem;
}

.p-3 {
  padding: 0.75rem;
}

.p-4 {
  padding: 1rem;
}

.p-5 {
  padding: 1.25rem;
}

.p-6 {
  padding: 1.5rem;
}

.\!px-3 {
  padding-left: 0.75rem !important;
  padding-right: 0.75rem !important;
}

.\!py-2 {
  padding-top: 0.5rem !important;
  padding-bottom: 0.5rem !important;
}

.\!py-2\.5 {
  padding-top: 0.625rem !important;
  padding-bottom: 0.625rem !important;
}

.px-2 {
  padding-left: 0.5rem;
  padding-right: 0.5rem;
}

.px-3 {
  padding-left: 0.75rem;
  padding-right: 0.75rem;
}

.px-4 {
  padding-left: 1rem;
  padding-right: 1rem;
}

.px-5 {
  padding-left: 1.25rem;
  padding-right: 1.25rem;
}

.py-0\.5 {
  padding-top: 0.125rem;
  padding-bottom: 0.125rem;
}

.py-2 {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
}

.py-2\.5 {
  padding-top: 0.625rem;
  padding-bottom: 0.625rem;
}

.py-3 {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
}

.py-8 {
  padding-top: 2rem;
  padding-bottom: 2rem;
}

.\!pl-9 {
  padding-left: 2.25rem !important;
}

.pb-2 {
  padding-bottom: 0.5rem;
}

.pb-24 {
  padding-bottom: 6rem;
}

.pb-28 {
  padding-bottom: 7rem;
}

.pb-3 {
  padding-bottom: 0.75rem;
}

.pb-4 {
  padding-bottom: 1rem;
}

.pl-9 {
  padding-left: 2.25rem;
}

.pr-1 {
  padding-right: 0.25rem;
}

.pr-3 {
  padding-right: 0.75rem;
}

.pt-3 {
  padding-top: 0.75rem;
}

.pt-4 {
  padding-top: 1rem;
}

.text-left {
  text-align: left;
}

.text-center {
  text-align: center;
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 2rem;
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 2.25rem;
}

.text-4xl {
  font-size: 2.25rem;
  line-height: 2.5rem;
}

.text-5xl {
  font-size: 3rem;
  line-height: 1;
}

.text-\[10px\] {
  font-size: 10px;
}

.text-\[110px\] {
  font-size: 110px;
}

.text-\[11px\] {
  font-size: 11px;
}

.text-\[13px\] {
  font-size: 13px;
}

.text-\[15px\] {
  font-size: 15px;
}

.text-\[18px\] {
  font-size: 18px;
}

.text-lg {
  font-size: 1.125rem;
  line-height: 1.75rem;
}

.text-sm {
  font-size: 0.875rem;
  line-height: 1.25rem;
}

.text-xl {
  font-size: 1.25rem;
  line-height: 1.75rem;
}

.text-xs {
  font-size: 0.75rem;
  line-height: 1rem;
}

.font-black {
  font-weight: 900;
}

.font-bold {
  font-weight: 700;
}

.font-extrabold {
  font-weight: 800;
}

.font-normal {
  font-weight: 400;
}

.font-semibold {
  font-weight: 600;
}

.italic {
  font-style: italic;
}

.leading-\[\.95\] {
  line-height: .95;
}

.leading-none {
  line-height: 1;
}

.leading-relaxed {
  line-height: 1.625;
}

.leading-tight {
  line-height: 1.25;
}

.tracking-\[\.18em\] {
  letter-spacing: .18em;
}

.tracking-widest {
  letter-spacing: 0.1em;
}

.\!text-\[\#5a4410\] {
  --tw-text-opacity: 1 !important;
  color: rgb(90 68 16 / var(--tw-text-opacity, 1)) !important;
}

.\!text-\[\#a9842c\] {
  --tw-text-opacity: 1 !important;
  color: rgb(169 132 44 / var(--tw-text-opacity, 1)) !important;
}

.\!text-\[\#e7c87a\] {
  --tw-text-opacity: 1 !important;
  color: rgb(231 200 122 / var(--tw-text-opacity, 1)) !important;
}

.\!text-white {
  --tw-text-opacity: 1 !important;
  color: rgb(255 255 255 / var(--tw-text-opacity, 1)) !important;
}

.text-\[\#071631\] {
  --tw-text-opacity: 1;
  color: rgb(7 22 49 / var(--tw-text-opacity, 1));
}

.text-\[\#5a4410\] {
  --tw-text-opacity: 1;
  color: rgb(90 68 16 / var(--tw-text-opacity, 1));
}

.text-\[\#a9842c\] {
  --tw-text-opacity: 1;
  color: rgb(169 132 44 / var(--tw-text-opacity, 1));
}

.text-\[\#e7c87a\] {
  --tw-text-opacity: 1;
  color: rgb(231 200 122 / var(--tw-text-opacity, 1));
}

.text-\[var\(--muted\)\] {
  color: var(--muted);
}

.text-amber-700 {
  --tw-text-opacity: 1;
  color: rgb(180 83 9 / var(--tw-text-opacity, 1));
}

.text-emerald-700 {
  --tw-text-opacity: 1;
  color: rgb(4 120 87 / var(--tw-text-opacity, 1));
}

.text-emerald-800 {
  --tw-text-opacity: 1;
  color: rgb(6 95 70 / var(--tw-text-opacity, 1));
}

.text-white {
  --tw-text-opacity: 1;
  color: rgb(255 255 255 / var(--tw-text-opacity, 1));
}

.text-white\/60 {
  color: rgb(255 255 255 / 0.6);
}

.text-white\/70 {
  color: rgb(255 255 255 / 0.7);
}

.text-white\/75 {
  color: rgb(255 255 255 / 0.75);
}

.text-white\/80 {
  color: rgb(255 255 255 / 0.8);
}

.opacity-15 {
  opacity: 0.15;
}

.opacity-80 {
  opacity: 0.8;
}

.outline-none {
  outline: 2px solid transparent;
  outline-offset: 2px;
}

.filter {
  filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
}

.transition {
  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform, filter, backdrop-filter;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

.transition-all {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
}

:root{
  --navy:#071631;
  --navy2:#0b254e;
  --navy3:#122f5c;
  --gold:#c9a24b;
  --gold2:#e7c87a;
  --gold3:#f4e3b0;
  --paper:#fbf7ee;
  --surface:#ffffff;
  --muted:#667085;
  --line:#e7ddc8;
  --ink:#101828
}

@media(prefers-color-scheme:dark){
  :root{
    --navy:#040c1d;
    --navy2:#071631;
    --paper:#0b1528;
    --surface:#101f3a;
    --muted:#a9b4c8;
    --line:#263752;
    --ink:#f2ead8
  }
}

*{
  box-sizing:border-box
}

html{
  scroll-behavior:smooth
}

body{
  margin:0;
  background:var(--paper);
  color:var(--ink);
  font-family:Manrope,system-ui,sans-serif
}

.font-display{
  font-family:Fraunces,Georgia,serif
}

.gold-line{
  background:linear-gradient(90deg,var(--gold),transparent)
}

.card{
  background:var(--surface);
  border:1px solid var(--line);
  border-radius:20px;
  box-shadow:0 10px 28px rgba(7,22,49,.06)
}

.chip{
  border:1px solid var(--line);
  border-radius:999px;
  padding:6px 10px;
  font-size:12px;
  font-weight:700;
  background:var(--surface)
}

.input{
  width:100%;
  border:1px solid var(--line);
  border-radius:12px;
  padding:11px 13px;
  background:var(--surface);
  color:var(--ink);
  font-size:14px;
  outline:none
}

.input:focus{
  border-color:var(--gold);
  box-shadow:0 0 0 3px rgba(201,162,75,.18)
}

.btn-gold{
  background:linear-gradient(135deg,#d6b25f,#a9842c);
  color:#fff;
  border:0;
  border-radius:12px;
  padding:12px 16px;
  font-weight:800;
  cursor:pointer
}

.btn-navy{
  background:var(--navy);
  color:#fff;
  border:0;
  border-radius:12px;
  padding:11px 15px;
  font-weight:700;
  cursor:pointer
}

.btn-ghost{
  background:transparent;
  border:1px solid var(--line);
  border-radius:12px;
  padding:10px 13px;
  font-weight:700;
  cursor:pointer;
  color:var(--ink)
}

.navbtn{
  white-space:nowrap;
  border:0;
  background:transparent;
  padding:9px 11px;
  border-radius:11px;
  font-weight:700;
  font-size:13px;
  cursor:pointer;
  color:var(--ink)
}

.navbtn.active{
  background:var(--navy);
  color:white
}

details summary{
  cursor:pointer;
  list-style:none
}

details summary::-webkit-details-marker{
  display:none
}

@keyframes fall{
  0%{
    transform:translateY(-20px) rotate(0)
  }

  100%{
    transform:translateY(520px) rotate(540deg);
    opacity:0
  }
}

.confetti{
  position:absolute;
  top:0;
  width:10px;
  height:16px;
  animation:fall 2.6s ease-in forwards
}

@keyframes floaty{
  0%,100%{
    transform:translateY(0)
  }

  50%{
    transform:translateY(-8px)
  }
}

.floaty{
  animation:floaty 3.5s ease-in-out infinite
}

.scrollbar-none::-webkit-scrollbar{
  display:none
}

.scrollbar-none{
  scrollbar-width:none
}

.placeholder\:text-white\/50::-moz-placeholder {
  color: rgb(255 255 255 / 0.5);
}

.placeholder\:text-white\/50::placeholder {
  color: rgb(255 255 255 / 0.5);
}

.last\:border-0:last-child {
  border-width: 0px;
}

.hover\:-translate-y-0\.5:hover {
  --tw-translate-y: -0.125rem;
  transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));
}

.hover\:bg-\[var\(--paper\)\]:hover {
  background-color: var(--paper);
}

.disabled\:opacity-40:disabled {
  opacity: 0.4;
}

.dark\:bg-\[var\(--surface\)\]:is(.dark *) {
  background-color: var(--surface);
}

@media (min-width: 640px) {
  .sm\:block {
    display: block;
  }

  .sm\:inline {
    display: inline;
  }

  .sm\:inline-flex {
    display: inline-flex;
  }

  .sm\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .sm\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .sm\:grid-cols-\[180px_150px_1fr\] {
    grid-template-columns: 180px 150px 1fr;
  }

  .sm\:place-items-center {
    place-items: center;
  }

  .sm\:p-9 {
    padding: 2.25rem;
  }

  .sm\:px-5 {
    padding-left: 1.25rem;
    padding-right: 1.25rem;
  }

  .sm\:text-2xl {
    font-size: 1.5rem;
    line-height: 2rem;
  }

  .sm\:text-4xl {
    font-size: 2.25rem;
    line-height: 2.5rem;
  }

  .sm\:text-\[22px\] {
    font-size: 22px;
  }
}

@media (min-width: 768px) {
  .md\:col-span-2 {
    grid-column: span 2 / span 2;
  }

  .md\:flex {
    display: flex;
  }

  .md\:hidden {
    display: none;
  }

  .md\:grid-cols-2 {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .md\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .lg\:sticky {
    position: sticky;
  }

  .lg\:top-24 {
    top: 6rem;
  }

  .lg\:block {
    display: block;
  }

  .lg\:grid {
    display: grid;
  }

  .lg\:hidden {
    display: none;
  }

  .lg\:grid-cols-3 {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }

  .lg\:grid-cols-4 {
    grid-template-columns: repeat(4, minmax(0, 1fr));
  }

  .lg\:grid-cols-\[1fr_380px\] {
    grid-template-columns: 1fr 380px;
  }

  .lg\:grid-cols-\[240px_1fr\] {
    grid-template-columns: 240px 1fr;
  }

  .lg\:grid-cols-\[380px_1fr\] {
    grid-template-columns: 380px 1fr;
  }

  .lg\:items-start {
    align-items: flex-start;
  }

  .lg\:gap-6 {
    gap: 1.5rem;
  }

  .lg\:pb-10 {
    padding-bottom: 2.5rem;
  }

  .lg\:pb-8 {
    padding-bottom: 2rem;
  }
}
</style>
</head>
<body>
  <div id="root"></div>

  <!-- React 18.3.1 (même version que celle intégrée dans le fichier d'origine), chargé depuis un CDN -->
  <script crossorigin src="https://unpkg.com/react@18.3.1/umd/react.production.min.js"></script>
  <script crossorigin src="https://unpkg.com/react-dom@18.3.1/umd/react-dom.production.min.js"></script>

  <script type="module">var Wd={default:window.React},Hd={createRoot:window.ReactDOM.createRoot,hydrateRoot:window.ReactDOM.hydrateRoot};var U=window.React;var Ru=window.React;var Ar=window.React;var Nd=window.React;var Ed=(e)=>e.replace(/([a-z0-9])([A-Z])/g,"$1-$2").toLowerCase(),Ou=(...e)=>e.filter((n,t,r)=>{return Boolean(n)&&n.trim()!==""&&r.indexOf(n)===t}).join(" ").trim();var _d={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:2,strokeLinecap:"round",strokeLinejoin:"round"};var Cd=Ar.forwardRef(({color:e="currentColor",size:n=24,strokeWidth:t=2,absoluteStrokeWidth:r,className:l="",children:u,iconNode:o,...i},c)=>{return Ar.createElement("svg",{ref:c,..._d,width:n,height:n,stroke:e,strokeWidth:r?Number(t)*24/Number(n):t,className:Ou("lucide",l),...i},[...o.map(([d,m])=>Ar.createElement(d,m)),...Array.isArray(u)?u:[u]])});var M=(e,n)=>{let t=Ru.forwardRef(({className:r,...l},u)=>Ru.createElement(Cd,{ref:u,iconNode:n,className:Ou(`lucide-${Ed(e)}`,r),...l}));return t.displayName=`${e}`,t};var Ir=M("ArrowRight",[["path",{d:"M5 12h14",key:"1ays0h"}],["path",{d:"m12 5 7 7-7 7",key:"xquz4c"}]]);var Wt=M("Award",[["path",{d:"m15.477 12.89 1.515 8.526a.5.5 0 0 1-.81.47l-3.58-2.687a1 1 0 0 0-1.197 0l-3.586 2.686a.5.5 0 0 1-.81-.469l1.514-8.526",key:"1yiouv"}],["circle",{cx:"12",cy:"8",r:"6",key:"1vp47v"}]]);var Yr=M("BookOpen",[["path",{d:"M12 7v14",key:"1akyts"}],["path",{d:"M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z",key:"ruj8y"}]]);var Un=M("ChevronRight",[["path",{d:"m9 18 6-6-6-6",key:"mthhwq"}]]);var Kr=M("Clock",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["polyline",{points:"12 6 12 12 16 14",key:"68esgv"}]]);var jn=M("Download",[["path",{d:"M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4",key:"ih7n3h"}],["polyline",{points:"7 10 12 15 17 10",key:"2ggqvy"}],["line",{x1:"12",x2:"12",y1:"15",y2:"3",key:"1vk2je"}]]);var Xr=M("FileText",[["path",{d:"M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z",key:"1rqfz7"}],["path",{d:"M14 2v4a2 2 0 0 0 2 2h4",key:"tnqrlb"}],["path",{d:"M10 9H8",key:"b1mrlr"}],["path",{d:"M16 13H8",key:"t4e002"}],["path",{d:"M16 17H8",key:"z1uh3a"}]]);var Zr=M("Gavel",[["path",{d:"m14.5 12.5-8 8a2.119 2.119 0 1 1-3-3l8-8",key:"15492f"}],["path",{d:"m16 16 6-6",key:"vzrcl6"}],["path",{d:"m8 8 6-6",key:"18bi4p"}],["path",{d:"m9 7 8 8",key:"5jnvq1"}],["path",{d:"m21 11-8-8",key:"z4y7zo"}]]);var Gr=M("Globe",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["path",{d:"M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20",key:"13o1zl"}],["path",{d:"M2 12h20",key:"9i4pu4"}]]);var Jr=M("Library",[["path",{d:"m16 6 4 14",key:"ji33uf"}],["path",{d:"M12 6v14",key:"1n7gus"}],["path",{d:"M8 8v12",key:"1gg7y9"}],["path",{d:"M4 4v16",key:"6qkkli"}]]);var xr=M("MessageCircle",[["path",{d:"M7.9 20A9 9 0 1 0 4 16.1L2 22Z",key:"vv11sd"}]]);var Mn=M("PenLine",[["path",{d:"M12 20h9",key:"t2du7b"}],["path",{d:"M16.376 3.622a1 1 0 0 1 3.002 3.002L7.368 18.635a2 2 0 0 1-.855.506l-2.872.838a.5.5 0 0 1-.62-.62l.838-2.872a2 2 0 0 1 .506-.854z",key:"1ykcvy"}]]);var qr=M("Scale",[["path",{d:"m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z",key:"7g6ntu"}],["path",{d:"m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z",key:"ijws7r"}],["path",{d:"M7 21h10",key:"1b0cd5"}],["path",{d:"M12 3v18",key:"108xh3"}],["path",{d:"M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2",key:"3gwbw2"}]]);var on=M("Search",[["circle",{cx:"11",cy:"11",r:"8",key:"4ej97u"}],["path",{d:"m21 21-4.3-4.3",key:"1qie3q"}]]);var Ht=M("Send",[["path",{d:"M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z",key:"1ffxy3"}],["path",{d:"m21.854 2.147-10.94 10.939",key:"12cjpa"}]]);var jr=M("Share2",[["circle",{cx:"18",cy:"5",r:"3",key:"gq8acd"}],["circle",{cx:"6",cy:"12",r:"3",key:"w7nqdw"}],["circle",{cx:"18",cy:"19",r:"3",key:"1xt0gg"}],["line",{x1:"8.59",x2:"15.42",y1:"13.51",y2:"17.49",key:"47mynk"}],["line",{x1:"15.41",x2:"8.59",y1:"6.51",y2:"10.49",key:"1n3mei"}]]);var br=M("ShieldCheck",[["path",{d:"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z",key:"oel41y"}],["path",{d:"m9 12 2 2 4-4",key:"dzmm74"}]]);var Fn=M("Sparkles",[["path",{d:"M9.937 15.5A2 2 0 0 0 8.5 14.063l-6.135-1.582a.5.5 0 0 1 0-.962L8.5 9.936A2 2 0 0 0 9.937 8.5l1.582-6.135a.5.5 0 0 1 .963 0L14.063 8.5A2 2 0 0 0 15.5 9.937l6.135 1.581a.5.5 0 0 1 0 .964L15.5 14.063a2 2 0 0 0-1.437 1.437l-1.582 6.135a.5.5 0 0 1-.963 0z",key:"4pj2yx"}],["path",{d:"M20 3v4",key:"1olli1"}],["path",{d:"M22 5h-4",key:"1gvqau"}],["path",{d:"M4 17v2",key:"vumght"}],["path",{d:"M5 18H3",key:"zchphs"}]]);var el=M("Users",[["path",{d:"M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2",key:"1yyitq"}],["circle",{cx:"9",cy:"7",r:"4",key:"nufk8"}],["path",{d:"M22 21v-2a4 4 0 0 0-3-3.87",key:"kshegd"}],["path",{d:"M16 3.13a4 4 0 0 1 0 7.75",key:"1da9ce"}]]);var Lt=M("X",[["path",{d:"M18 6 6 18",key:"1bl5f8"}],["path",{d:"m6 6 12 12",key:"d8bk6v"}]]);var D1=Symbol.for("react.element");var $1=Object.prototype.hasOwnProperty,B1=Nd.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner,V1={key:!0,ref:!0,__self:!0,__source:!0};function Pd(e,n,t){var r,l={},u=null,o=null;t!==void 0&&(u=""+t),n.key!==void 0&&(u=""+n.key),n.ref!==void 0&&(o=n.ref);for(r in n)$1.call(n,r)&&!V1.hasOwnProperty(r)&&(l[r]=n[r]);if(e&&e.defaultProps)for(r in n=e.defaultProps,n)l[r]===void 0&&(l[r]=n[r]);return{$$typeof:D1,type:e,key:u,ref:o,props:l,_owner:B1.current}}var a=Pd,h=Pd;var W1=(e,n,t)=>`DÉFINITION — ${t}
Dans le cadre de « ${n} » en ${e}, « ${t.toLowerCase()} » désigne une notion structurante du raisonnement juridique. Elle permet d’identifier la règle applicable, de qualifier les faits et d’ordonner les arguments. Comme toute notion de droit, elle ne se comprend pas isolément : elle s’articule avec les principes généraux, la hiérarchie des normes et la pratique des juridictions.

PRINCIPES DIRECTEURS
• Légalité : aucune solution ne peut être fondée sur une règle inexistante ou inapplicable aux faits.
• Proportionnalité : la réponse juridique doit rester adaptée à la gravité, à l’enjeu et au préjudice.
• Sécurité juridique : les parties doivent pouvoir prévoir les conséquences de leurs actes.
• Contradictoire : chaque partie doit pouvoir connaître les arguments adverses et y répondre.
• Motivation : toute décision doit être expliquée en fait et en droit.

MÉTHODE EN 4 TEMPS
1) Qualifier les faits : qui sont les parties, quel est l’acte, quel est le dommage ou le litige ?
2) Identifier la branche du droit et la règle applicable.
3) Vérifier les conditions d’application : délai, forme, compétence, qualité pour agir.
4) Conclure : sanction, effet, voie de recours ou clause à rédiger.

EXEMPLE CONCRET
Un étudiant loue un logement sans état des lieux détaillé. À la sortie, le bailleur retient le dépôt de garantie. L’analyse commence par la qualification du contrat de bail, puis par la preuve de l’état du logement, avant d’examiner la restitution, la retenue justifiée et la juridiction compétente. Le même raisonnement — faits, règle, conditions, solution — s’applique à un contrat, à un licenciement ou à un litige foncier.

JURISPRUDENCE ET PRATIQUE
Les juges contrôlent la qualification retenue, la bonne application de la règle et la motivation. Une décision insuffisamment motivée ou fondée sur une qualification erronée peut être censurée en appel ou en cassation. C’est pourquoi la rédaction juridique exige des phrases courtes, des références précises et une distinction nette entre le fait allégué et le fait prouvé.

À RETENIR
Retenez la définition, les quatre principes, la méthode en quatre temps et l’exemple. Pour réviser, reformulez la notion sans regarder vos notes, puis testez-la sur un cas nouveau. C’est cette capacité à passer du cours au cas pratique qui fait la différence à l’examen et dans la pratique.`;function A(e,n,t,r,l){let u=l.map((o,i)=>{let c=[["Fondements et définitions","Cadre et portée"],["Régime et mise en œuvre","Contrôle et sanction"]];return{title:`Chapitre ${i+1} — ${o}`,sections:c.map(([d,m],g)=>{let y=(E,_)=>({title:`${i+1}.${g+1}.${_+1} ${E}`,lessons:[{title:`Leçon : ${E}`,body:W1(e,o,E)}]});return{title:`Section ${i+1}.${g+1} — ${g===0?d:m}`,subs:[y(`Les notions essentielles de ${o.toLowerCase()}`,0),y("Les conditions d’application",1)]}})}});return{name:e,code:n,desc:t,prof:r,chapters:u}}var Uu=[{id:"L1",title:"Licence 1",subtitle:"Les fondations du droit",color:"#c9a24b",matieres:[A("Introduction au Droit","L1-01","La notion, les sources et l’organisation du droit.","Pr. N’Guessan",["Notion de droit et caractères de la règle","Les sources du droit","L’organisation judiciaire","La preuve et les personnes"]),A("Droit Constitutionnel","L1-02","Constitution, État et séparation des pouvoirs.","Dr. Koffi",["L’État et la Constitution","La séparation des pouvoirs","Les droits fondamentaux","Les régimes politiques"]),A("Droit Civil 1 — Personnes & Famille","L1-03","Personnalité, filiation, mariage et régimes.","Pr. Diallo",["La personnalité juridique","Le mariage et le divorce","La filiation","La protection des majeurs"]),A("Histoire du Droit","L1-04","Des droits antiques aux codifications.","Dr. Traoré",["Les droits anciens","Le droit romain","L’Ancien Régime","Les grandes codifications"]),A("Droit Administratif 1","L1-05","Administration, acte administratif et service public.","Pr. Koné",["L’administration et ses missions","L’acte administratif","Le service public","Le contrôle de l’administration"]),A("Économie Politique","L1-06","Marché, État et politiques publiques.","Dr. Mensah",["Les acteurs économiques","Le marché et la concurrence","La monnaie et l’inflation","La croissance et le développement"]),A("Relations Internationales","L1-07","États, organisations et ordre international.","Pr. Diop",["Les acteurs internationaux","La souveraineté","Les organisations internationales","La paix et la sécurité"]),A("Méthodologie Juridique","L1-08","Dissertation, commentaire et cas pratique.","Dr. Yao",["La dissertation juridique","Le commentaire d’arrêt","Le cas pratique","La recherche documentaire"])]},{id:"L2",title:"Licence 2",subtitle:"Le raisonnement et les obligations",color:"#e7c87a",matieres:[A("Droit des Obligations","L2-01","Contrat, responsabilité et quasi-contrats.","Pr. N’Guessan",["La formation du contrat","L’exécution du contrat","La responsabilité civile","Les quasi-contrats"]),A("Droit Pénal Général","L2-02","Infraction, responsabilité et peine.","Dr. Koffi",["L’infraction","L’auteur et le complice","La responsabilité pénale","La peine et son application"]),A("Droit Administratif 2","L2-03","Responsabilité et contrats administratifs.","Pr. Koné",["La responsabilité administrative","Les contrats administratifs","Le domaine public","Le recours pour excès de pouvoir"]),A("Droit des Affaires","L2-04","Commerçant, actes de commerce et fonds.","Dr. Mensah",["Le commerçant","Les actes de commerce","Le fonds de commerce","Les effets de commerce"]),A("Droit Fiscal","L2-05","Impôt, assiette et contrôle fiscal.","Pr. Diallo",["Les principes de l’impôt","L’impôt sur le revenu","La TVA","Le contrôle et le contentieux"]),A("Droit International Public","L2-06","Traités, responsabilité et juridictions.","Pr. Diop",["Les sources du droit international","Les traités","La responsabilité internationale","Les juridictions internationales"]),A("Droit Civil 2 — Biens","L2-07","Propriété, possession et démembrements.","Dr. Traoré",["La propriété","La possession","L’usufruit et la servitude","La copropriété"]),A("Procédure Civile","L2-08","Action, instance et voies de recours.","Dr. Yao",["L’action en justice","L’instance","Le jugement","Les voies de recours"])]},{id:"L3",title:"Licence 3",subtitle:"La spécialisation et la pratique",color:"#a9842c",matieres:[A("Droit des Contrats Spéciaux","L3-01","Vente, bail, mandat et contrats nommés.","Pr. N’Guessan",["La vente","Le bail","Le mandat","Le prêt et le dépôt"]),A("Droit Pénal Spécial","L3-02","Atteintes aux personnes, aux biens et à la société.","Dr. Koffi",["Les atteintes aux personnes","Les atteintes aux biens","Les infractions économiques","Les infractions contre l’État"]),A("Droit du Travail","L3-01","Contrat de travail, licenciement et négociation.","Pr. Koné",["Le contrat de travail","La durée et la rémunération","Le licenciement","Les relations collectives"]),A("Droit des Sociétés","L3-04","Création, fonctionnement et dissolution.","Dr. Mensah",["Les formes de sociétés","La création de la société","Le fonctionnement","La dissolution et la liquidation"]),A("Droit International Privé","L3-05","Conflits de lois et de juridictions.","Pr. Diop",["Le conflit de lois","Le conflit de juridictions","La nationalité","La condition des étrangers"]),A("Procédure Pénale","L3-06","Enquête, poursuite et jugement pénal.","Dr. Yao",["L’enquête","La poursuite","L’instruction","Le procès pénal"]),A("Droit de l’Environnement","L3-07","Pollution, responsabilité et protection.","Pr. Diallo",["Les principes environnementaux","La pollution","La responsabilité écologique","Les aires protégées"]),A("Droit OHADA","L3-08","Actes uniformes et CCJA.","Pr. Traoré",["Présentation de l’OHADA","Les Actes uniformes","La CCJA","L’arbitrage OHADA"])]}],H1=[{t:"Présentation de l’OHADA",d:"Organisation pour l’Harmonisation en Afrique du Droit des Affaires : 17 États, un droit harmonisé pour sécuriser les affaires, les investissements et les échanges.",q:"OHADA"},{t:"Droit commercial général",d:"Commerçant, registre du commerce, bail commercial, intermédiaires et vente commerciale. Le statut du commerçant suppose immatriculation et tenue d’une comptabilité.",q:"OHADA"},{t:"Droit des sociétés commerciales & GIE",d:"Sociétés en nom collectif, SARL, SA, SAS. Constitution, apports, organes, responsabilité des dirigeants et dissolution.",q:"OHADA"},{t:"Sûretés",d:"Cautionnement, nantissement, gage, hypothèque, droit de rétention. La sûreté garantit le paiement d’une dette par un bien ou un garant.",q:"OHADA"},{t:"Procédures collectives",d:"Règlement préventif, redressement judiciaire et liquidation. Objectif : sauvegarder l’entreprise, maintenir l’emploi et payer les créanciers.",q:"OHADA"},{t:"Arbitrage",d:"Convention d’arbitrage, tribunal arbitral, sentence et recours devant la CCJA. L’arbitrage offre rapidité, confidentialité et exécution facilitée.",q:"OHADA"},{t:"Comptabilité & information financière",d:"Plan comptable OHADA, états financiers, audit. La transparence comptable protège associés, créanciers et investisseurs.",q:"OHADA"},{t:"Transport de marchandises par route",d:"Contrat de transport, responsabilité du transporteur, délais et indemnisation en cas de perte ou d’avarie.",q:"OHADA"},{t:"Médiation",d:"Processus amiable guidé par un tiers neutre. La médiation préserve la relation et aboutit à un accord exécutoire.",q:"OHADA"},{t:"La CCJA",d:"Cour Commune de Justice et d’Arbitrage : elle assure l’interprétation uniforme des Actes uniformes et juge en cassation.",q:"OHADA"}],zd=[{t:"Abus de droit",d:"Exercice d’un droit de manière à causer un préjudice anormal à autrui, dépassant son utilité légitime.",s:"Détournement de droit",e:"Un propriétaire construit un mur uniquement pour priver son voisin de lumière."},{t:"Acte juridique",d:"Manifestation de volonté destinée à produire des effets de droit : contrat, testament, donation.",s:"Negotium",e:"La signature d’un contrat de vente est un acte juridique."},{t:"Alinéa",d:"Subdivision d’un article de loi, introduite par un retour à la ligne.",s:"Paragraphe",e:"L’article 2, alinéa 3 du code civil."},{t:"Amnistie",d:"Loi qui efface le caractère infractionnel de certains faits et leurs conséquences pénales.",s:"Pardon légal",e:"Une loi d’amnistie peut effacer certaines condamnations."},{t:"Appel",d:"Voie de recours qui permet de faire rejuger une affaire en fait et en droit par une juridiction supérieure.",s:"Recours",e:"L’appel doit être formé dans le délai légal."},{t:"Arrêt",d:"Décision rendue par une juridiction supérieure : cour d’appel, Cour suprême ou CCJA.",s:"Décision",e:"L’arrêt de la Cour a cassé le jugement."},{t:"Assignation",d:"Acte par lequel un demandeur appelle une personne à comparaître devant un tribunal.",s:"Citation",e:"L’assignation est signifiée par un commissaire de justice."},{t:"Aveu",d:"Reconnaissance par une partie d’un fait qui lui est défavorable.",s:"Confession",e:"L’aveu peut être judiciaire ou extrajudiciaire."},{t:"Bail",d:"Contrat par lequel une personne donne à une autre la jouissance d’une chose moyennant un loyer.",s:"Location",e:"Le bail d’habitation encadre les droits du locataire."},{t:"Cassation",d:"Annulation par la juridiction suprême d’une décision rendue en violation du droit.",s:"Annulation",e:"Le pourvoi en cassation ne rejugue pas les faits."},{t:"Clause",d:"Disposition particulière d’un acte ou d’un contrat.",s:"Stipulation",e:"La clause de non-concurrence limite l’activité après le contrat."},{t:"Comparution",d:"Fait de se présenter devant une juridiction ou une autorité.",s:"Présentation",e:"La comparution immédiate accélère le procès pénal."},{t:"Contrat",d:"Accord de volontés destiné à créer des obligations entre les parties.",s:"Convention",e:"Le contrat doit respecter le consentement, l’objet et la cause."},{t:"Délibéré",d:"Période pendant laquelle les juges examinent l’affaire avant de rendre leur décision.",s:"Délibération",e:"L’affaire a été mise en délibéré au 12 mai."},{t:"Délit",d:"Infraction de gravité moyenne, punie d’une peine correctionnelle.",s:"Infraction",e:"Le vol simple est un délit."},{t:"Divorce",d:"Dissolution du mariage prononcée par le juge ou constatée selon les formes légales.",s:"Rupture du mariage",e:"Le divorce par consentement mutuel suppose un accord complet."},{t:"Dommages-intérêts",d:"Somme versée pour réparer un préjudice subi.",s:"Indemnité",e:"La victime a obtenu des dommages-intérêts pour son préjudice moral."},{t:"Droit subjectif",d:"Prérogative reconnue à une personne par le droit objectif.",s:"Prérogative",e:"Le droit de propriété est un droit subjectif."},{t:"Exequatur",d:"Décision qui rend exécutoire dans un État une décision étrangère ou une sentence arbitrale.",s:"Homologation",e:"La sentence arbitrale nécessite l’exequatur."},{t:"Filiation",d:"Lien juridique qui unit un enfant à son père ou à sa mère.",s:"Parenté",e:"La filiation peut être établie par l’acte de naissance."},{t:"Garde d’enfant",d:"Organisation de la résidence, de l’éducation et des visites de l’enfant après séparation.",s:"Garde",e:"Le juge fixe la garde selon l’intérêt de l’enfant."},{t:"Héritier",d:"Personne appelée à recueillir tout ou partie d’une succession.",s:"Successeur",e:"Les héritiers doivent accepter ou renoncer à la succession."},{t:"Hypothèque",d:"Sûreté réelle portant sur un immeuble, sans dépossession du débiteur.",s:"Garantie immobilière",e:"La banque prend une hypothèque sur la maison."},{t:"Infraction",d:"Comportement interdit et sanctionné par la loi pénale.",s:"Fait punissable",e:"Toute infraction suppose un élément légal, matériel et moral."},{t:"Jurisprudence",d:"Ensemble des décisions rendues par les juridictions et qui interprètent le droit.",s:"Décisions",e:"La jurisprudence de la CCJA uniformise le droit OHADA."},{t:"Légitime défense",d:"Cause d’irresponsabilité lorsque l’on riposte de façon proportionnée à une agression actuelle et injuste.",s:"Défense",e:"La riposte doit être proportionnée à l’attaque."},{t:"Mandat",d:"Acte par lequel une personne donne à une autre le pouvoir d’agir en son nom.",s:"Procuration",e:"Le mandat de vente permet au mandataire de signer."},{t:"Nullité",d:"Sanction qui prive un acte de ses effets pour vice de formation ou de fond.",s:"Annulation",e:"Le contrat conclu sans consentement est frappé de nullité."},{t:"Obligation",d:"Lien de droit par lequel une personne doit donner, faire ou ne pas faire quelque chose.",s:"Engagement",e:"Le vendeur a l’obligation de délivrer la chose."},{t:"Prescription",d:"Délai au-delà duquel une action ou une poursuite ne peut plus être exercée.",s:"Délai",e:"La prescription de l’action civile est encadrée par la loi."},{t:"Procureur",d:"Magistrat chargé de représenter l’intérêt général et d’exercer l’action publique.",s:"Ministère public",e:"Le procureur requiert l’application de la loi."},{t:"Quitus",d:"Décharge donnée à une personne de sa gestion.",s:"Décharge",e:"L’assemblée donne quitus au gérant."},{t:"Recours",d:"Voie permettant de contester une décision devant une juridiction.",s:"Contestation",e:"Le recours gracieux s’adresse à l’auteur de la décision."},{t:"Responsabilité civile",d:"Obligation de réparer le dommage causé à autrui par sa faute, sa négligence ou sa chose.",s:"Réparation",e:"La responsabilité civile suppose faute, dommage et lien de causalité."},{t:"Saisie",d:"Mesure qui place un bien sous main de justice pour garantir le paiement d’une créance.",s:"Mesure d’exécution",e:"La saisie-attribution bloque les sommes dues."},{t:"Servitude",d:"Charge imposée à un fonds au profit d’un autre fonds.",s:"Charge foncière",e:"La servitude de passage permet d’accéder à une parcelle enclavée."},{t:"Testament",d:"Acte par lequel une personne dispose de tout ou partie de ses biens pour après son décès.",s:"Dispositions de dernière volonté",e:"Le testament olographe doit être écrit, daté et signé."},{t:"Tutelle",d:"Mesure de protection d’un mineur ou d’un majeur vulnérable.",s:"Protection",e:"Le tuteur représente le mineur dans les actes civils."},{t:"Usufruit",d:"Droit d’utiliser un bien et d’en percevoir les fruits, sans en être propriétaire.",s:"Démembrement",e:"La veuve peut bénéficier de l’usufruit du logement."},{t:"Vice de consentement",d:"Erreur, dol ou violence qui altère la volonté et peut entraîner la nullité du contrat.",s:"Vice",e:"Le dol vicie le consentement de la victime."},{t:"Voie de fait",d:"Comportement manifestement illégal accompli sans droit par l’administration ou un particulier.",s:"Illégalité flagrante",e:"La démolition sans décision est une voie de fait."},{t:"Acte authentique",d:"Acte reçu par un officier public avec les solennités requises et qui fait foi jusqu’à inscription de faux.",s:"Acte notarié",e:"La vente immobilière peut être reçue par notaire."},{t:"Action en justice",d:"Droit de saisir un juge pour faire reconnaître ou protéger un droit.",s:"Action",e:"L’action doit être fondée sur un intérêt légitime."},{t:"Bonne foi",d:"Comportement loyal et honnête exigé dans la formation et l’exécution des actes juridiques.",s:"Loyauté",e:"Les contrats doivent être exécutés de bonne foi."},{t:"Capacité juridique",d:"Aptitude à être titulaire de droits et à les exercer.",s:"Capacité",e:"Le mineur a une capacité d’exercice réduite."},{t:"Concubinage",d:"Union de fait entre deux personnes qui vivent en couple sans être mariées.",s:"Union libre",e:"Le concubinage ne produit pas les mêmes effets que le mariage."},{t:"Contentieux",d:"Ensemble des litiges portés devant une juridiction.",s:"Litige",e:"Le contentieux fiscal oppose le contribuable à l’administration."},{t:"Déchéance",d:"Perte d’un droit à la suite d’une sanction ou de l’écoulement d’un délai.",s:"Perte de droit",e:"La déchéance de l’autorité parentale est prononcée par le juge."},{t:"Emprisonnement",d:"Peine privative de liberté exécutée dans un établissement pénitentiaire.",s:"Détention",e:"L’emprisonnement peut être assorti du sursis."},{t:"Faute",d:"Manquement à une obligation ou à un devoir de prudence qui cause un dommage.",s:"Manquement",e:"La faute doit être prouvée par la victime."},{t:"Garantie",d:"Engagement d’assurer une personne contre un risque ou un défaut.",s:"Protection",e:"Le vendeur doit la garantie des vices cachés."},{t:"Homicide",d:"Fait de donner la mort à une personne, volontairement ou involontairement.",s:"Meurtre",e:"L’homicide involontaire résulte d’une imprudence."},{t:"Immunité",d:"Protection qui empêche certaines poursuites contre une personne en raison de sa fonction.",s:"Protection",e:"L’immunité parlementaire encadre les poursuites."},{t:"Juge des référés",d:"Juge saisi en urgence pour prendre une mesure provisoire.",s:"Juge d’urgence",e:"Le référé permet d’obtenir une mesure rapide."},{t:"Loi",d:"Règle générale et obligatoire votée par le Parlement et promulguée.",s:"Texte",e:"Nul n’est censé ignorer la loi."},{t:"Mineur",d:"Personne âgée de moins de 18 ans, soumise à un régime de protection.",s:"Enfant",e:"Le mineur est représenté par ses parents."},{t:"Notaire",d:"Officier public chargé de recevoir les actes authentiques et de conseiller les parties.",s:"Officier public",e:"Le notaire authentifie la vente."},{t:"Ordonnance",d:"Décision rendue par un juge statuant seul, souvent en urgence ou en matière d’instruction.",s:"Décision",e:"Le juge a rendu une ordonnance de référé."},{t:"Partie civile",d:"Victime qui se joint à l’action publique pour obtenir réparation.",s:"Victime",e:"La partie civile demande des dommages-intérêts."},{t:"Quorum",d:"Nombre minimal de membres présents pour qu’une assemblée délibère valablement.",s:"Seuil",e:"Le quorum n’était pas atteint, la réunion est reportée."},{t:"Récidive",d:"Fait de commettre une nouvelle infraction après une condamnation définitive.",s:"Répétition",e:"La récidive aggrave la peine."},{t:"Sursis",d:"Mesure qui suspend l’exécution d’une peine sous conditions.",s:"Suspension",e:"La peine est assortie du sursis simple."},{t:"Témoin",d:"Personne qui relate des faits dont elle a eu connaissance.",s:"Déposant",e:"Le témoin doit dire la vérité."},{t:"Ultra petita",d:"Décision qui dépasse ce qui a été demandé par les parties.",s:"Excès",e:"Le juge ne doit pas statuer ultra petita."},{t:"Vol",d:"Soustraction frauduleuse de la chose d’autrui.",s:"Soustraction",e:"Le vol suppose l’appréhension d’une chose appartenant à autrui."},{t:"Zèle",d:"Ardeur excessive dans l’exercice d’une fonction, parfois source d’excès.",s:"Excès de zèle",e:"L’excès de zèle peut engager la responsabilité."},{t:"Abrogation",d:"Suppression d’une règle de droit par une règle nouvelle.",s:"Suppression",e:"La loi nouvelle abroge la loi ancienne."},{t:"Adoption",d:"Création d’un lien de filiation par décision judiciaire.",s:"Filiation adoptive",e:"L’adoption confère à l’enfant les droits d’un enfant légitime."},{t:"Arbitrage",d:"Mode de règlement des litiges par un tribunal privé choisi par les parties.",s:"Justice privée",e:"L’arbitrage OHADA est régi par un Acte uniforme."},{t:"Bénéficiaire",d:"Personne qui reçoit un avantage, une somme ou un droit.",s:"Destinataire",e:"Le bénéficiaire de l’assurance reçoit le capital."},{t:"Citation",d:"Acte qui convoque une personne devant une juridiction.",s:"Convocation",e:"La citation indique la date d’audience."},{t:"Débiteur",d:"Personne tenue d’exécuter une obligation envers un créancier.",s:"Obligé",e:"Le débiteur doit payer à l’échéance."},{t:"Émancipation",d:"Acte qui confère à un mineur la capacité d’un majeur.",s:"Anticipation de majorité",e:"L’émancipation permet au mineur de gérer certains actes."},{t:"Fonds de commerce",d:"Ensemble des éléments utilisés pour exploiter une activité commerciale.",s:"Fonds",e:"La vente du fonds comprend la clientèle."},{t:"Greffe",d:"Service d’une juridiction qui conserve les actes et assiste les juges.",s:"Secrétariat du tribunal",e:"Le greffe délivre la copie du jugement."},{t:"Huissier",d:"Officier ministériel chargé de signifier les actes et d’exécuter les décisions.",s:"Commissaire de justice",e:"Le commissaire de justice signifie l’assignation."},{t:"Injonction",d:"Ordre donné par un juge de faire ou de ne pas faire quelque chose.",s:"Ordre",e:"L’injonction de payer permet de recouvrer une créance."},{t:"Juridiction",d:"Organe chargé de trancher les litiges en appliquant le droit.",s:"Tribunal",e:"La juridiction compétente dépend de la nature du litige."},{t:"Litige",d:"Contestation qui oppose des parties sur un droit.",s:"Différend",e:"Les parties cherchent à régler leur litige à l’amiable."},{t:"Médiation",d:"Processus amiable où un tiers neutre aide les parties à trouver un accord.",s:"Conciliation",e:"La médiation OHADA favorise le règlement amiable."},{t:"Notification",d:"Fait de porter un acte ou une décision à la connaissance d’une personne.",s:"Information",e:"La notification marque le début du délai de recours."},{t:"Opposition",d:"Voie de recours contre une décision rendue par défaut.",s:"Recours",e:"L’opposition permet de faire rejuger l’affaire."},{t:"Pourvoi",d:"Recours porté devant la juridiction suprême.",s:"Recours en cassation",e:"Le pourvoi doit être formé dans le délai légal."},{t:"Réconciliation",d:"Rétablissement d’une entente entre parties en conflit.",s:"Accord",e:"La réconciliation met fin au conflit familial."},{t:"Séquestre",d:"Mesure qui place un bien litigieux sous la garde d’un tiers.",s:"Garde",e:"Le bien est mis sous séquestre en attendant le jugement."},{t:"Transaction",d:"Contrat par lequel les parties terminent un litige par des concessions réciproques.",s:"Accord transactionnel",e:"La transaction a l’autorité de la chose jugée."},{t:"Usucapion",d:"Acquisition de la propriété par la possession prolongée pendant un certain délai.",s:"Prescription acquisitive",e:"La possession paisible peut conduire à l’usucapion."},{t:"Vente",d:"Contrat par lequel une personne transfère la propriété d’une chose moyennant un prix.",s:"Cession",e:"La vente est parfaite dès l’accord sur la chose et le prix."},{t:"Acompte",d:"Somme versée d’avance sur le prix d’une prestation ou d’un bien.",s:"Avance",e:"L’acompte engage les parties à conclure."},{t:"Astreinte",d:"Somme due par jour de retard en cas d’inexécution d’une décision.",s:"Pénalité",e:"Le juge assortit l’injonction d’une astreinte."},{t:"Avocat",d:"Professionnel du droit qui conseille, assiste et représente ses clients.",s:"Défenseur",e:"L’avocat plaide devant la juridiction."},{t:"Caution",d:"Personne qui s’engage à payer si le débiteur principal ne paie pas.",s:"Garant",e:"La caution peut être poursuivie en cas de défaillance."},{t:"Délai de grâce",d:"Délai accordé par le juge au débiteur pour payer sa dette.",s:"Report",e:"Le juge peut accorder un délai de grâce."},{t:"Expertise",d:"Mesure d’instruction confiée à un spécialiste pour éclairer le juge.",s:"Examen technique",e:"L’expertise médicale évalue le préjudice."},{t:"Force majeure",d:"Événement imprévisible, irrésistible et extérieur qui exonère de responsabilité.",s:"Cas de force majeure",e:"La catastrophe naturelle peut constituer un cas de force majeure."},{t:"Héritage",d:"Ensemble des biens transmis après le décès d’une personne.",s:"Succession",e:"L’héritage est partagé entre les héritiers."},{t:"Indivision",d:"Situation où plusieurs personnes sont propriétaires ensemble d’un même bien.",s:"Copropriété",e:"L’indivision prend fin par le partage."},{t:"Jugement",d:"Décision rendue par un tribunal de première instance.",s:"Décision",e:"Le jugement est susceptible d’appel."},{t:"Légataire",d:"Personne qui reçoit un legs par testament.",s:"Bénéficiaire testamentaire",e:"Le légataire reçoit le bien désigné."},{t:"Motivation",d:"Exposé des raisons de fait et de droit qui fondent une décision.",s:"Justification",e:"La motivation est une garantie contre l’arbitraire."},{t:"Nantissement",d:"Sûreté qui affecte un bien meuble ou une créance en garantie d’une dette.",s:"Gage",e:"Le nantissement de parts sociales doit être publié."},{t:"Offre",d:"Proposition de contracter adressée à une personne déterminée ou au public.",s:"Proposition",e:"L’offre doit être précise et ferme."},{t:"Plainte",d:"Acte par lequel une victime porte à la connaissance de la justice une infraction.",s:"Dénonciation",e:"La plainte peut être déposée au commissariat."},{t:"Quittance",d:"Écrit qui constate le paiement d’une somme.",s:"Reçu",e:"Le bailleur délivre une quittance de loyer."},{t:"Réparation",d:"Action de remettre en état ou d’indemniser un dommage.",s:"Indemnisation",e:"La réparation peut être en nature ou en argent."},{t:"Sommation",d:"Mise en demeure faite par un officier ministériel.",s:"Mise en demeure",e:"La sommation de payer précède la saisie."},{t:"Tutelle — suite",d:"Voir Tutelle : mesure de protection organisée par le juge.",s:"Protection",e:"Le conseil de famille assiste le tuteur."},{t:"Audience",d:"Séance publique au cours de laquelle une juridiction entend les parties.",s:"Séance",e:"L’audience est présidée par le juge."},{t:"Déclaration",d:"Acte par lequel une personne fait connaître un fait ou une volonté.",s:"Affirmation",e:"La déclaration de naissance doit être faite rapidement."},{t:"État civil",d:"Ensemble des actes qui constatent la situation d’une personne : naissance, mariage, décès.",s:"Registre",e:"L’état civil prouve l’identité."},{t:"Fonction publique",d:"Ensemble des emplois permanents des administrations et des agents qui les occupent.",s:"Administration",e:"Le fonctionnaire est soumis à un statut."},{t:"Interdiction",d:"Défense faite par la loi ou par le juge d’accomplir un acte.",s:"Prohibition",e:"L’interdiction de gérer sanctionne certains dirigeants."},{t:"Liberté provisoire",d:"Mesure qui permet à une personne poursuivie de rester libre en attendant son jugement.",s:"Mise en liberté",e:"La liberté provisoire peut être assortie de conditions."},{t:"Obligation alimentaire",d:"Devoir de fournir à un proche les moyens nécessaires à sa subsistance.",s:"Pension alimentaire",e:"Le parent doit verser une pension alimentaire."},{t:"Possession",d:"Fait d’exercer sur une chose les pouvoirs du propriétaire.",s:"Détention",e:"La possession doit être paisible et publique."},{t:"Régime matrimonial",d:"Ensemble de règles qui organise les rapports patrimoniaux entre époux.",s:"Régime",e:"Le régime de la communauté est le régime légal."},{t:"Société",d:"Contrat par lequel des personnes mettent en commun des biens ou leur industrie pour partager les bénéfices.",s:"Personne morale",e:"La société acquiert la personnalité morale par immatriculation."},{t:"Vente aux enchères",d:"Vente publique où le bien est adjugé au plus offrant.",s:"Adjudication",e:"La vente aux enchères est organisée par un officier public."},{t:"Zonage",d:"Découpage d’un territoire en zones soumises à des règles d’urbanisme différentes.",s:"Planification",e:"Le zonage détermine les constructions autorisées."}],Td=[["A priori","À partir de ce qui précède ; sans tenir compte de l’expérience."],["A posteriori","À partir de l’expérience ; après les faits."],["Ad hoc","Pour ce cas précis ; spécialement créé pour la circonstance."],["Ad litem","Pour le procès ; mandataire désigné pour un litige."],["A fortiori","À plus forte raison."],["Alibi","Ailleurs ; preuve que l’accusé était ailleurs au moment des faits."],["Amicus curiae","Ami de la cour ; personne qui éclaire le juge sans être partie."],["Animus","Intention, volonté."],["Bona fide","De bonne foi."],["Casus belli","Événement qui justifie une guerre ou un conflit."],["Ceteris paribus","Toutes choses égales par ailleurs."],["Contra legem","Contre la loi."],["Corpus delicti","Corps du délit ; éléments matériels de l’infraction."],["De facto","En fait, dans la réalité."],["De jure","En droit, selon la loi."],["Erga omnes","À l’égard de tous ; opposable à tout le monde."],["Ex aequo et bono","Selon l’équité et le bien."],["Ex nihilo","À partir de rien."],["Ex officio","D’office, en vertu de sa fonction."],["Ex post facto","Après les faits ; rétroactivement."],["Habeas corpus","Que tu aies le corps ; garantie contre la détention arbitraire."],["In camera","À huis clos."],["In flagrante delicto","En flagrant délit."],["In dubio pro reo","Dans le doute, en faveur de l’accusé."],["In pari causa","Dans une cause égale."],["In solidum","Solidairement."],["In toto","Dans son ensemble."],["Inter alia","Entre autres choses."],["Inter partes","Entre les parties."],["Ipso facto","Par le fait même."],["Ipso jure","Par le droit lui-même, automatiquement."],["Jus cogens","Norme impérative du droit international."],["Jus gentium","Droit des gens."],["Jus in bello","Droit applicable pendant la guerre."],["Jus ad bellum","Droit de recourir à la guerre."],["Lex loci","Loi du lieu."],["Lex specialis","Loi spéciale qui déroge à la loi générale."],["Lex posterior","Loi postérieure."],["Lex fori","Loi du for, du tribunal saisi."],["Modus operandi","Manière d’opérer."],["Mutatis mutandis","En changeant ce qui doit être changé."],["Ne bis in idem","Pas deux fois pour la même chose."],["Nemo dat","Nul ne donne ce qu’il n’a pas."],["Non bis in idem","Interdiction d’être jugé deux fois pour les mêmes faits."],["Nulla poena sine lege","Pas de peine sans loi."],["Nullum crimen sine lege","Pas de crime sans loi."],["Pacta sunt servanda","Les conventions doivent être respectées."],["Pater familias","Père de famille ; personne prudente et diligente."],["Per se","En soi."],["Prima facie","À première vue."],["Pro bono","Pour le bien public ; gratuitement."],["Pro rata","En proportion."],["Pro tempore","Pour le moment."],["Quid pro quo","Quelque chose pour quelque chose."],["Ratio decidendi","Motif déterminant de la décision."],["Ratio legis","Raison de la loi."],["Res judicata","Chose jugée."],["Res nullius","Chose sans maître."],["Sine qua non","Condition indispensable."],["Status quo","État actuel des choses."],["Sub judice","Pendant devant le juge ; en cours de jugement."],["Sui generis","En son genre ; unique."],["Sui juris","Capable de se gouverner soi-même."],["Ultra vires","Au-delà des pouvoirs."],["Ubi jus, ibi remedium","Là où il y a un droit, il y a un remède."],["Verbatim","Mot pour mot."],["Vice versa","Réciproquement."],["Vis major","Force majeure."],["Vox populi","Voix du peuple."],["Actus reus","Acte coupable ; élément matériel de l’infraction."],["Mens rea","Intention coupable ; élément moral."],["Nul ne peut se prévaloir de sa propre turpitude","On ne peut invoquer sa propre faute pour obtenir un avantage."],["Nul n’est censé ignorer la loi","Chacun est présumé connaître la loi."],["Le doute profite à l’accusé","En cas de doute, le juge doit relaxer ou acquitter."],["La plume est serve, la parole est libre","Le procureur écrit selon sa hiérarchie, mais plaide librement."],["Dura lex, sed lex","La loi est dure, mais c’est la loi."],["Ignorantia juris non excusat","L’ignorance du droit n’excuse pas."],["Innocent jusqu’à preuve du contraire","Présomption d’innocence."],["Audi alteram partem","Écoutez l’autre partie."],["Nemo judex in causa sua","Nul n’est juge dans sa propre cause."],["Ubi lex non distinguit","Là où la loi ne distingue pas, on ne doit pas distinguer."],["Lex retro non agit","La loi ne rétroagit pas."],["Salus populi suprema lex","Le salut du peuple est la loi suprême."],["Summum jus, summa injuria","Le droit poussé à l’extrême devient la pire injustice."],["Fiat justitia ruat caelum","Que justice soit faite, même si le ciel doit s’écrouler."],["Justitia omnibus","La justice pour tous."],["Locus standi","Qualité pour agir en justice."],["Obiter dictum","Remarque incidente, sans force obligatoire."],["Per incuriam","Par inadvertance ; décision rendue sans tenir compte d’un texte."],["Stare decisis","S’en tenir à ce qui a été décidé."],["Sine die","Sans fixer de date."],["Ad referendum","Sous réserve d’approbation."],["Ad valorem","Selon la valeur."],["Bona vacantia","Biens sans maître."],["Coram nobis","Devant nous ; recours devant la même juridiction."],["De minimis","De peu d’importance."],["Ex parte","D’une seule partie, sans l’autre."],["In limine","Au seuil ; dès le début."],["Inter se","Entre eux."],["Jus soli","Droit du sol."],["Jus sanguinis","Droit du sang."],["Locus delicti","Lieu du délit."],["Mala in se","Mauvais en soi."],["Mala prohibita","Mauvais parce que prohibé."],["Nemo tenetur se ipsum accusare","Nul n’est tenu de s’accuser lui-même."],["Pari passu","À égalité, au même rang."],["Persona non grata","Personne non désirée."],["Quantum meruit","Autant que mérité ; rémunération proportionnée."],["Res gestae","Choses faites ; faits liés à l’événement."],["Sine die — audience","Audience renvoyée sans date."],["Tabula rasa","Table rase."],["Terra nullius","Terre sans maître."],["Veto","J’oppose ; droit de s’opposer."],["A contrario","À l’inverse."],["A minima","Au minimum."],["Ad infinitum","À l’infini."],["De novo","À nouveau."],["Ex gratia","Par faveur, sans obligation."],["In extremis","À la dernière extrémité."],["In situ","Sur place."],["Lex mercatoria","Droit des marchands."],["Nunc pro tunc","Maintenant pour alors ; rétroactivement."],["Pro forma","Pour la forme."],["Sine loco","Sans lieu."]],Od=[{cat:"L1",q:"Qu’est-ce que la règle de droit ?",opts:["Une simple habitude","Une règle générale, obligatoire et sanctionnée","Un conseil moral","Une décision politique"],ans:1,ex:"La règle de droit est générale, obligatoire, et son non-respect est sanctionné."},{cat:"L1",q:"Quelle est la hiérarchie la plus élevée en droit interne ?",opts:["Le règlement","La loi","La Constitution","La circulaire"],ans:2,ex:"La Constitution est au sommet de la hiérarchie des normes internes."},{cat:"L1",q:"Le consentement dans un contrat doit être :",opts:["Vicié","Libre et éclairé","Forcé","Implicite seulement"],ans:1,ex:"Un consentement vicié par erreur, dol ou violence peut entraîner la nullité."},{cat:"L1",q:"La séparation des pouvoirs distingue :",opts:["Législatif, exécutif, judiciaire","Public et privé","Civil et pénal","National et local"],ans:0,ex:"Montesquieu distingue législatif, exécutif et judiciaire."},{cat:"L1",q:"Qu’est-ce que la jurisprudence ?",opts:["Un recueil de lois","L’ensemble des décisions des juridictions","Un traité","Un règlement"],ans:1,ex:"Elle interprète le droit à travers les décisions rendues."},{cat:"L1",q:"La personnalité juridique commence en principe à :",opts:["La conception toujours","La naissance","La majorité","L’école"],ans:1,ex:"Elle commence à la naissance vivante et viable."},{cat:"L1",q:"Un fait juridique se distingue de l’acte juridique car il est :",opts:["Voulu","Non voulu pour produire des effets de droit","Toujours écrit","Toujours un contrat"],ans:1,ex:"Le fait juridique produit des effets sans volonté de les produire."},{cat:"L1",q:"Le commentaire d’arrêt exige d’abord :",opts:["Recopier l’arrêt","Dégager le problème de droit","Critiquer le juge","Inventer une solution"],ans:1,ex:"Il faut identifier les faits, la procédure et le problème de droit."},{cat:"L1",q:"La loi est votée par :",opts:["Le juge","Le Parlement","Le maire seul","Le procureur"],ans:1,ex:"Le Parlement vote la loi, promulguée ensuite."},{cat:"L1",q:"Un droit subjectif est :",opts:["Une règle générale","Une prérogative d’une personne","Une sanction","Une coutume"],ans:1,ex:"Ex. : droit de propriété, droit de créance."},{cat:"L1",q:"La coutume est une source :",opts:["Écrite obligatoire","Non écrite fondée sur la pratique","Uniquement pénale","Internationale seulement"],ans:1,ex:"Elle naît d’une pratique répétée et d’un sentiment d’obligation."},{cat:"L1",q:"L’état civil prouve :",opts:["La richesse","L’identité et la situation familiale","Le diplôme","La nationalité seule"],ans:1,ex:"Naissance, mariage, décès y sont constatés."},{cat:"L1",q:"La preuve en droit civil repose souvent sur :",opts:["La parole seule","L’écrit pour les actes importants","Le hasard","L’opinion"],ans:1,ex:"L’écrit est souvent exigé au-delà d’un certain montant."},{cat:"L1",q:"Le mariage crée :",opts:["Aucun effet","Des droits et devoirs entre époux","Un contrat commercial","Une société"],ans:1,ex:"Fidélité, secours, assistance, contribution aux charges."},{cat:"L1",q:"La dissertation juridique comporte :",opts:["Une seule partie","Introduction, développement, conclusion","Un récit","Un poème"],ans:1,ex:"Le plan en deux parties est classique et équilibré."},{cat:"L2",q:"La responsabilité civile suppose :",opts:["Faute, dommage, lien de causalité","Richesse, âge, sexe","Contrat seul","Sanction pénale"],ans:0,ex:"Les trois conditions sont cumulatives."},{cat:"L2",q:"L’infraction pénale suppose :",opts:["Un élément légal, matériel et moral","Une seule volonté","Un dommage","Une plainte"],ans:0,ex:"Sans texte, pas d’infraction : nullum crimen sine lege."},{cat:"L2",q:"Le recours pour excès de pouvoir conteste :",opts:["Un contrat privé","Un acte administratif illégal","Un jugement pénal","Un testament"],ans:1,ex:"Il permet d’annuler un acte administratif illégal."},{cat:"L2",q:"Le commerçant doit :",opts:["Être mineur","S’immatriculer au registre du commerce","Ne pas tenir de comptabilité","Éviter les impôts"],ans:1,ex:"L’immatriculation est une condition du statut."},{cat:"L2",q:"La TVA est un impôt :",opts:["Direct","Indirect sur la consommation","Sur la fortune","Local"],ans:1,ex:"Elle est collectée par les entreprises et supportée par le consommateur."},{cat:"L2",q:"Le traité international entre en vigueur après :",opts:["Un simple discours","Signature et ratification","Un tweet","Un vote local"],ans:1,ex:"La ratification exprime le consentement définitif."},{cat:"L2",q:"L’usufruit permet de :",opts:["Vendre le bien","Utiliser le bien et percevoir ses fruits","Détruire le bien","Changer le propriétaire"],ans:1,ex:"Le nu-propriétaire conserve la propriété."},{cat:"L2",q:"L’appel permet :",opts:["De rejuger en fait et en droit","De confirmer toujours","De changer de loi","D’annuler la Constitution"],ans:0,ex:"C’est une voie de recours ordinaire."},{cat:"L2",q:"La prescription extinctive éteint :",opts:["La loi","L’action après un délai","Le contrat immédiatement","Le juge"],ans:1,ex:"Au-delà du délai, l’action n’est plus recevable."},{cat:"L2",q:"Le fonds de commerce comprend :",opts:["Uniquement le local","Clientèle, enseigne, matériel","Les dettes personnelles","Le domicile"],ans:1,ex:"La clientèle en est l’élément essentiel."},{cat:"L2",q:"La légitime défense exige :",opts:["Une riposte disproportionnée","Une riposte proportionnée à une agression injuste","Une vengeance","Un délai long"],ans:1,ex:"La proportionnalité est une condition clé."},{cat:"L2",q:"La responsabilité administrative peut être engagée :",opts:["Sans faute, pour risque","Jamais","Seulement pour faute lourde","Uniquement en pénal"],ans:0,ex:"La responsabilité sans faute existe pour risque ou rupture d’égalité."},{cat:"L2",q:"La servitude est :",opts:["Une charge sur un fonds au profit d’un autre","Un impôt","Un contrat de travail","Une peine"],ans:0,ex:"Ex. : servitude de passage."},{cat:"L2",q:"La saisine du juge suppose :",opts:["Un intérêt à agir","Une fortune","Un avocat toujours","Un procès pénal"],ans:0,ex:"L’intérêt doit être légitime, né et actuel."},{cat:"L2",q:"Le dol est :",opts:["Une erreur spontanée","Une manœuvre pour tromper","Une violence","Un oubli"],ans:1,ex:"Il vicie le consentement."},{cat:"L3",q:"Le contrat de travail suppose :",opts:["Un lien de subordination","Une simple amitié","Un stage","Une vente"],ans:0,ex:"Prestation, rémunération et subordination le caractérisent."},{cat:"L3",q:"Un licenciement doit reposer sur :",opts:["Un caprice","Un motif réel et sérieux","Une rumeur","Un retard unique sans procédure"],ans:1,ex:"La procédure et le motif sont contrôlés par le juge."},{cat:"L3",q:"La SARL est :",opts:["Une société de personnes sans limite","Une société à responsabilité limitée","Un contrat de bail","Une association"],ans:1,ex:"Les associés ne répondent qu’à hauteur de leurs apports."},{cat:"L3",q:"Le conflit de lois en droit international privé porte sur :",opts:["La loi applicable à une situation internationale","La couleur des drapeaux","Le choix du juge seul","La langue"],ans:0,ex:"La règle de conflit désigne la loi applicable."},{cat:"L3",q:"La procédure pénale commence souvent par :",opts:["Le jugement","L’enquête","La peine","L’appel"],ans:1,ex:"Enquête, poursuite, instruction puis jugement."},{cat:"L3",q:"Le principe pollueur-payeur signifie :",opts:["L’État paie toujours","Le pollueur supporte le coût de la pollution","La victime paie","Personne ne paie"],ans:1,ex:"C’est un principe du droit de l’environnement."},{cat:"L3",q:"La vente est parfaite dès :",opts:["La livraison","L’accord sur la chose et le prix","Le paiement","La signature du notaire"],ans:1,ex:"Le transfert de propriété peut suivre cet accord."},{cat:"L3",q:"La clause de non-concurrence doit être :",opts:["Illimitée","Limitée dans le temps, l’espace et indemnisée","Secrète","Orale"],ans:1,ex:"Sans limites, elle peut être jugée abusive."},{cat:"L3",q:"L’assemblée générale d’une société :",opts:["Ne décide rien","Approuve les comptes et décide des grandes orientations","Paye les impôts","Rédige les contrats"],ans:1,ex:"Elle est un organe essentiel de décision."},{cat:"L3",q:"La garde d’enfant est fixée selon :",opts:["La richesse","L’intérêt supérieur de l’enfant","Le premier demandeur","Le hasard"],ans:1,ex:"Le juge apprécie chaque situation."},{cat:"L3",q:"Le bail commercial protège :",opts:["Le locataire contre l’expulsion sans indemnité","Le bailleur seul","Le voisin","L’État"],ans:0,ex:"Le droit au renouvellement est central."},{cat:"L3",q:"La dissolution d’une société entraîne :",opts:["Sa disparition immédiate","Sa liquidation","Un nouveau contrat","Une fusion"],ans:1,ex:"La liquidation permet de payer les créanciers et partager le reliquat."},{cat:"L3",q:"Le droit pénal spécial étudie :",opts:["Les infractions en particulier","La procédure civile","Les contrats","La famille"],ans:0,ex:"Vol, escroquerie, homicide, etc."},{cat:"L3",q:"L’instruction pénale est dirigée par :",opts:["Le juge d’instruction","Le maire","L’avocat","Le greffier"],ans:0,ex:"Il instruit à charge et à décharge."},{cat:"L3",q:"La protection de l’environnement vise :",opts:["À détruire la nature","À prévenir et réparer les atteintes","À interdire toute activité","À taxer les pauvres"],ans:1,ex:"Prévention, précaution et réparation."},{cat:"OHADA",q:"L’OHADA signifie :",opts:["Organisation pour l’Harmonisation en Afrique du Droit des Affaires","Office des Hautes Autorités","Organisation Humanitaire","Office du Droit"],ans:0,ex:"Elle harmonise le droit des affaires dans 17 États membres."},{cat:"OHADA",q:"La CCJA est :",opts:["Une banque","La Cour Commune de Justice et d’Arbitrage","Un parlement","Une université"],ans:1,ex:"Elle assure l’interprétation uniforme des Actes uniformes."},{cat:"OHADA",q:"L’Acte uniforme sur les sûretés régit :",opts:["Le mariage","Cautionnement, gage, hypothèque","Le divorce","Les élections"],ans:1,ex:"Il sécurise le crédit."},{cat:"OHADA",q:"L’arbitrage OHADA permet :",opts:["De juger sans loi","Un règlement rapide et confidentiel des litiges","D’éviter tout contrat","De condamner pénalement"],ans:1,ex:"La sentence peut obtenir l’exequatur."},{cat:"OHADA",q:"Le règlement préventif vise à :",opts:["Liquider immédiatement","Éviter la cessation des paiements","Augmenter les dettes","Fermer l’entreprise"],ans:1,ex:"Il anticipe les difficultés."},{cat:"OHADA",q:"Le bail commercial OHADA exige :",opts:["Un écrit et un loyer","Un simple handshake","Un notaire obligatoire","Une durée d’un jour"],ans:0,ex:"Il encadre le statut du preneur et le renouvellement."},{cat:"OHADA",q:"La médiation est :",opts:["Un procès","Un processus amiable avec un tiers neutre","Une sanction","Une saisie"],ans:1,ex:"Elle préserve la relation commerciale."},{cat:"OHADA",q:"Un Acte uniforme est :",opts:["Une simple recommandation","Directement applicable dans les États membres","Une loi nationale","Un traité de paix"],ans:1,ex:"Il s’applique sans transposition."},{cat:"OHADA",q:"La comptabilité OHADA impose :",opts:["Des états financiers fiables","Aucune comptabilité","Des comptes secrets","Un seul bilan"],ans:0,ex:"Transparence pour associés et créanciers."},{cat:"OHADA",q:"Le transport OHADA régit :",opts:["Le transport de marchandises par route","Le transport aérien seul","Le mariage","Les impôts"],ans:0,ex:"Responsabilité du transporteur en cas de perte ou d’avarie."}],Mu=["Prof","Enseignant","Docteur","Juriste","Juge","Avocat","Procureur","Étudiant","Autre"],Rd=["Licenciement","Dette","Terre / Foncier","Divorce","Vol","Viol","Contrat","Crime","Harcèlement","Succession","Accident","Bail","Garde d’enfant"],L1=["Droit Pénal","Droit Civil","OHADA","Droit du Travail","Débats & Actualité"],Q1=["Qu’est-ce qu’un contrat valable ?","Comment contester un licenciement ?","Que faire en cas de divorce ?","Qu’est-ce que l’OHADA ?","Comment récupérer une dette ?","Quels sont mes droits en cas de vol ?","Terrain : que vérifier avant d’acheter ?","Que faire en cas de harcèlement ?","Comment organiser la garde d’enfant ?","Que faire après un accident ?","Qu’est-ce qu’une société ?","Comment contester une décision ?"];function Ud(e){let n=e.toLowerCase();if(n.includes("contrat"))return`CONTRAT VALABLE — 4 CONDITIONS
1) Consentement libre et éclairé
2) Capacité des parties
3) Objet licite et déterminé
4) Cause licite

ÉTAPES : négocier, vérifier les clauses, signer, conserver une preuve. En cas de vice (erreur, dol, violence), le contrat peut être annulé. Astuce : lisez la clause de résiliation, la durée et les pénalités avant de signer.`;if(n.includes("licenciement"))return`LICENCIEMENT — VÉRIFIEZ
• Motif réel et sérieux
• Procédure : convocation, entretien, notification
• Délais et indemnités
• Possibilité de contestation devant l’inspection du travail ou le tribunal

Conservez tous les écrits : lettre, bulletins, contrat. Ne signez aucun document sous pression sans le relire.`;if(n.includes("divorce"))return`DIVORCE — PARCOURS
1) Choisir le type : consentement mutuel ou contentieux
2) Régler la résidence des enfants, la pension, le partage des biens
3) Saisir le juge avec les pièces d’état civil et financières

L’intérêt de l’enfant reste prioritaire. Un accord écrit facilite et accélère la procédure.`;if(n.includes("ohada"))return`OHADA — L’ESSENTIEL
Organisation pour l’Harmonisation en Afrique du Droit des Affaires. Ses Actes uniformes s’appliquent directement : droit commercial, sociétés, sûretés, procédures collectives, arbitrage, comptabilité, transport, médiation. La CCJA assure l’interprétation uniforme et tranche en cassation.`;if(n.includes("dette"))return`DETTE — QUE FAIRE ?
1) Réunir les preuves : contrat, factures, messages, reçus
2) Relancer par écrit avec un délai précis
3) Proposer un échéancier écrit
4) En cas d’échec : mise en demeure, médiation, puis saisine du juge

Ne payez jamais sans quittance. Une reconnaissance de dette écrite protège les deux parties.`;if(n.includes("vol"))return`VOL — RÉFLEXES
1) Mettre les personnes en sécurité
2) Déposer plainte avec la liste des biens, factures et photos
3) Prévenir l’assurance et la banque si besoin
4) Conserver toute preuve : vidéos, témoins, traces

Le vol est une infraction pénale. La victime peut se constituer partie civile pour obtenir réparation.`;if(n.includes("bail")||n.includes("loyer"))return`BAIL — POINTS CLÉS
Le bail fixe le loyer, la durée, l’état des lieux et les obligations. Le locataire doit payer et entretenir ; le bailleur doit délivrer un logement décent. À la sortie, l’état des lieux comparatif détermine la restitution du dépôt de garantie.`;if(n.includes("succession")||n.includes("héritage"))return`SUCCESSION — ÉTAPES
1) Acte de décès et inventaire des biens
2) Identification des héritiers et du testament éventuel
3) Acceptation ou renonciation
4) Partage amiable ou judiciaire

Un notaire sécurise le partage. Ne vendez pas un bien indivis sans l’accord de tous.`;if(n.includes("foncier")||n.includes("terre")||n.includes("terrain")||n.includes("parcelle"))return`FONCIER / TERRE — DÉFINITION
Le droit foncier organise la propriété et l’usage du sol.
ÉTAPES : 1) Vérifier le titre foncier et le plan 2) Consulter l’historique au service des domaines 3) Exiger un acte écrit et un bornage 4) Éviter l’achat sur simple reçu.
PRINCIPE : seul un titre régulier sécurise la propriété.
CONSEIL : consultez un avocat ou un notaire avant tout paiement.`;if(n.includes("viol")||n.includes("agression sexuelle"))return`VIOL / AGRESSION — DÉFINITION
Le viol est une infraction pénale grave, caractérisée par un acte imposé sans consentement.
ÉTAPES : 1) Se mettre en sécurité 2) Se faire accompagner médicalement et psychologiquement 3) Déposer plainte et conserver les preuves 4) Demander protection et réparation.
PRINCIPE : le consentement doit être libre et éclairé.
CONSEIL : consultez un avocat et une association d’aide aux victimes. Ceci est une aide pédagogique, pas un conseil d’avocat.`;if(n.includes("crime")||n.includes("meurtre")||n.includes("homicide"))return`CRIME — DÉFINITION
Le crime est l’infraction la plus grave, jugée selon une procédure pénale renforcée.
ÉTAPES : 1) Sécuriser les personnes 2) Alerter les autorités 3) Préserver les preuves 4) Constitution de partie civile pour la victime.
PRINCIPE : présomption d’innocence et procès équitable.
CONSEIL : consultez un avocat.`;if(n.includes("harcèlement")||n.includes("harcelement"))return`HARCÈLEMENT — DÉFINITION
Des propos ou comportements répétés qui dégradent les conditions de vie ou de travail.
ÉTAPES : 1) Conserver les messages et dates 2) Alerter l’employeur ou l’établissement 3) Déposer plainte si nécessaire 4) Demander protection et accompagnement.
PRINCIPE : nul ne doit subir des agissements répétés portant atteinte à sa dignité.
CONSEIL : consultez un avocat.`;if(n.includes("garde")||n.includes("enfant"))return`GARDE D’ENFANT — DÉFINITION
Organisation de la résidence, de l’éducation et des visites après séparation.
ÉTAPES : 1) Chercher un accord écrit 2) Fixer résidence, visites et pension 3) Saisir le juge si désaccord 4) Réviser si la situation change.
PRINCIPE : l’intérêt supérieur de l’enfant prime.
CONSEIL : consultez un avocat.`;if(n.includes("accident"))return`ACCIDENT — DÉFINITION
Événement soudain causant un dommage corporel ou matériel.
ÉTAPES : 1) Secourir et sécuriser 2) Constater les faits, photos, témoins 3) Déclarer à l’assurance 4) Évaluer le préjudice et demander réparation.
PRINCIPE : la responsabilité suppose faute, dommage et lien de causalité.
CONSEIL : consultez un avocat.`;if(n.includes("société")||n.includes("societe")||n.includes("sarl")||n.includes("entreprise"))return`SOCIÉTÉ — DÉFINITION
Contrat par lequel des personnes mettent en commun des biens ou leur industrie pour partager les bénéfices.
ÉTAPES : 1) Choisir la forme (SARL, SA, SAS…) 2) Rédiger les statuts 3) Immatriculer 4) Organiser organes et comptes.
PRINCIPE : la société acquiert la personnalité morale par immatriculation.
CONSEIL : consultez un avocat.`;if(n.includes("travail")||n.includes("salaire")||n.includes("contrat de travail"))return`DROIT DU TRAVAIL — DÉFINITION
Il encadre le contrat de travail, la rémunération, la durée et la rupture.
ÉTAPES : 1) Vérifier le contrat 2) Conserver bulletins et horaires 3) Respecter la procédure 4) Contester devant l’inspection ou le tribunal.
PRINCIPE : le lien de subordination caractérise le contrat de travail.
CONSEIL : consultez un avocat.`;if(n.includes("impôt")||n.includes("impot")||n.includes("fiscal")||n.includes("tva"))return`FISCAL — DÉFINITION
Le droit fiscal organise l’impôt, son assiette et son contrôle.
ÉTAPES : 1) Identifier l’impôt 2) Vérifier la base et le taux 3) Déclarer dans le délai 4) Contester par réclamation puis recours.
PRINCIPE : l’impôt doit être prévu par la loi.
CONSEIL : consultez un avocat ou un fiscaliste.`;if(n.includes("administratif")||n.includes("mairie")||n.includes("administration"))return`DROIT ADMINISTRATIF — DÉFINITION
Il encadre l’administration, ses actes et le service public.
ÉTAPES : 1) Identifier l’acte 2) Vérifier compétence, forme et motif 3) Former un recours gracieux 4) Saisir le juge administratif.
PRINCIPE : l’administration agit selon la légalité.
CONSEIL : consultez un avocat.`;if(n.includes("constitution")||n.includes("constitutionnel"))return`DROIT CONSTITUTIONNEL — DÉFINITION
Il organise l’État, les pouvoirs et les droits fondamentaux.
ÉTAPES : 1) Identifier la norme 2) Vérifier la hiérarchie 3) Contrôler la conformité 4) Invoquer les droits fondamentaux.
PRINCIPE : la Constitution est au sommet de la hiérarchie interne.
CONSEIL : consultez un avocat.`;if(n.includes("pénal")||n.includes("penal")||n.includes("peine")||n.includes("prison"))return`DROIT PÉNAL — DÉFINITION
Il définit les infractions et les peines.
ÉTAPES : 1) Vérifier le texte 2) Caractériser l’élément matériel et moral 3) Identifier la peine 4) Garantir les droits de la défense.
PRINCIPE : pas de peine sans loi.
CONSEIL : consultez un avocat.`;if(n.includes("civil")||n.includes("responsabilité"))return`DROIT CIVIL — DÉFINITION
Il régit les personnes, les biens, les obligations et la famille.
ÉTAPES : 1) Qualifier les faits 2) Identifier la règle 3) Vérifier faute, dommage et lien de causalité 4) Demander réparation.
PRINCIPE : chacun répond du dommage causé.
CONSEIL : consultez un avocat.`;if(n.includes("preuve"))return`PREUVE — DÉFINITION
Tout moyen de démontrer un fait ou un acte.
ÉTAPES : 1) Identifier ce qu’il faut prouver 2) Choisir l’écrit, le témoignage ou l’expertise 3) Conserver les originaux 4) Présenter au juge.
PRINCIPE : celui qui allègue doit prouver.
CONSEIL : consultez un avocat.`;if(n.includes("mariage")||n.includes("fiançailles"))return`MARIAGE — DÉFINITION
Union légale créant droits et devoirs entre époux.
ÉTAPES : 1) Vérifier les conditions 2) Choisir le régime matrimonial 3) Célébrer selon les formes 4) Respecter fidélité, secours et contribution.
PRINCIPE : le mariage suppose un consentement libre.
CONSEIL : consultez un avocat.`;if(n.includes("testament"))return`TESTAMENT — DÉFINITION
Acte par lequel une personne dispose de ses biens après son décès.
ÉTAPES : 1) Rédiger, dater et signer 2) Désigner les bénéficiaires 3) Conserver chez un notaire 4) Respecter les héritiers réservataires.
PRINCIPE : le testament olographe doit être écrit, daté et signé.
CONSEIL : consultez un notaire.`;if(n.includes("hypothèque")||n.includes("hypotheque")||n.includes("garantie")||n.includes("caution"))return`GARANTIE / SÛRETÉ — DÉFINITION
Mécanisme qui garantit le paiement d’une dette.
ÉTAPES : 1) Identifier la sûreté 2) Vérifier sa forme et sa publicité 3) Respecter l’échéance 4) En cas d’impayé, mettre en œuvre la garantie.
PRINCIPE : la sûreté suit la dette principale.
CONSEIL : consultez un avocat.`;if(n.includes("arbitrage")||n.includes("médiation")||n.includes("mediation")||n.includes("conciliation"))return`MODES AMIABLES — DÉFINITION
Arbitrage, médiation et conciliation règlent un litige sans procès classique.
ÉTAPES : 1) Choisir le mode 2) Désigner un tiers neutre 3) Négocier 4) Formaliser l’accord ou la sentence.
PRINCIPE : l’accord amiable préserve la relation.
CONSEIL : consultez un avocat.`;if(n.includes("appel")||n.includes("cassation")||n.includes("recours"))return`VOIES DE RECOURS — DÉFINITION
Moyens de contester une décision.
ÉTAPES : 1) Vérifier le délai 2) Choisir appel, opposition ou pourvoi 3) Motiver le recours 4) Respecter la forme.
PRINCIPE : le délai est strict et le recours doit être motivé.
CONSEIL : consultez un avocat.`;if(n.includes("nationalité")||n.includes("nationalite")||n.includes("étranger")||n.includes("etranger"))return`NATIONALITÉ — DÉFINITION
Lien juridique qui rattache une personne à un État.
ÉTAPES : 1) Identifier le mode d’acquisition 2) Réunir l’état civil 3) Déposer la demande 4) Respecter les délais.
PRINCIPE : la nationalité se prouve par des actes.
CONSEIL : consultez un avocat.`;if(n.includes("environnement")||n.includes("pollution"))return`ENVIRONNEMENT — DÉFINITION
Il protège la nature et organise la prévention des atteintes.
ÉTAPES : 1) Identifier la pollution 2) Conserver les preuves 3) Alerter l’autorité 4) Demander prévention et réparation.
PRINCIPE : pollueur-payeur.
CONSEIL : consultez un avocat.`;if(n.includes("santé")||n.includes("sante")||n.includes("médical")||n.includes("medical"))return`SANTÉ — DÉFINITION
Le droit de la santé encadre les soins, le consentement et la responsabilité médicale.
ÉTAPES : 1) Demander l’information 2) Donner un consentement éclairé 3) Conserver le dossier 4) En cas de faute, demander expertise.
PRINCIPE : le patient doit être informé.
CONSEIL : consultez un avocat.`;if(n.includes("numérique")||n.includes("numerique")||n.includes("internet")||n.includes("données")||n.includes("donnees"))return`NUMÉRIQUE — DÉFINITION
Il protège les données, la vie privée et les échanges en ligne.
ÉTAPES : 1) Identifier le traitement 2) Vérifier le consentement 3) Exercer les droits d’accès et de rectification 4) Signaler un abus.
PRINCIPE : les données personnelles doivent être traitées loyalement.
CONSEIL : consultez un avocat.`;if(n.includes("vente")||n.includes("achat"))return`VENTE — DÉFINITION
Contrat qui transfère la propriété moyennant un prix.
ÉTAPES : 1) S’accorder sur la chose et le prix 2) Vérifier les vices 3) Rédiger l’acte 4) Livrer et payer.
PRINCIPE : la vente est parfaite dès l’accord sur la chose et le prix.
CONSEIL : consultez un avocat.`;if(n.includes("propriété")||n.includes("propriete")||n.includes("possession"))return`PROPRIÉTÉ — DÉFINITION
Droit d’user, de jouir et de disposer d’une chose.
ÉTAPES : 1) Prouver le titre 2) Vérifier les charges 3) Protéger la possession 4) Agir contre les troubles.
PRINCIPE : la propriété est un droit fondamental, mais encadré.
CONSEIL : consultez un avocat.`;if(n.includes("famille"))return`DROIT DE LA FAMILLE — DÉFINITION
Il régit mariage, filiation, divorce et protection des enfants.
ÉTAPES : 1) Identifier la situation 2) Réunir l’état civil 3) Chercher un accord 4) Saisir le juge si nécessaire.
PRINCIPE : l’intérêt de l’enfant prime.
CONSEIL : consultez un avocat.`;if(n.includes("mineur")||n.includes("enfance"))return`MINEUR — DÉFINITION
Personne de moins de 18 ans soumise à une protection particulière.
ÉTAPES : 1) Identifier le représentant 2) Protéger l’enfant 3) Saisir le juge si danger 4) Adapter les actes à l’âge.
PRINCIPE : la protection de l’enfant est prioritaire.
CONSEIL : consultez un avocat.`;if(n.includes("avocat")||n.includes("juge")||n.includes("procureur")||n.includes("notaire"))return`ACTEURS DE LA JUSTICE — DÉFINITION
Juge, avocat, procureur et notaire ont des rôles distincts.
ÉTAPES : 1) Identifier le bon interlocuteur 2) Préparer les pièces 3) Poser une question précise 4) Conserver les écrits.
PRINCIPE : chacun agit dans ses compétences.
CONSEIL : consultez un avocat pour votre cas.`;if(n.includes("délai")||n.includes("delai")||n.includes("prescription"))return`DÉLAI / PRESCRIPTION — DÉFINITION
Période au-delà de laquelle une action ne peut plus être exercée.
ÉTAPES : 1) Identifier le point de départ 2) Calculer le délai 3) Agir avant l’échéance 4) Conserver la preuve de l’envoi.
PRINCIPE : le délai protège la sécurité juridique.
CONSEIL : consultez un avocat.`;if(n.includes("contrat de travail")||n.includes("démission")||n.includes("demission"))return`DÉMISSION — DÉFINITION
Rupture du contrat de travail à l’initiative du salarié.
ÉTAPES : 1) Rédiger une démission claire 2) Respecter le préavis 3) Remettre les documents 4) Vérifier les droits.
PRINCIPE : la démission doit être libre et sans ambiguïté.
CONSEIL : consultez un avocat.`;if(n.includes("stage")||n.includes("université")||n.includes("universite")||n.includes("examen")||n.includes("diplôme")||n.includes("diplome"))return`ÉTUDES / EXAMEN — DÉFINITION
Les règles universitaires encadrent inscription, examens et diplômes.
ÉTAPES : 1) Lire le règlement 2) Respecter les délais 3) Conserver les convocations 4) Contester par recours gracieux si nécessaire.
PRINCIPE : toute décision doit être motivée.
CONSEIL : consultez le service de scolarité puis un avocat si besoin.`;if(n.includes("assurance"))return`ASSURANCE — DÉFINITION
Contrat qui garantit contre un risque moyennant une prime.
ÉTAPES : 1) Déclarer le sinistre 2) Conserver les preuves 3) Respecter le délai 4) Contester l’offre si elle est insuffisante.
PRINCIPE : la bonne foi est exigée des deux parties.
CONSEIL : consultez un avocat.`;if(n.includes("banque")||n.includes("crédit")||n.includes("credit")||n.includes("prêt")||n.includes("pret"))return`BANQUE / CRÉDIT — DÉFINITION
Le crédit engage l’emprunteur à rembourser selon un échéancier.
ÉTAPES : 1) Lire le taux et les frais 2) Vérifier la capacité de remboursement 3) Conserver le contrat 4) Négocier en cas de difficulté.
PRINCIPE : l’emprunteur doit être informé.
CONSEIL : consultez un avocat.`;if(n.includes("commerce")||n.includes("commerçant")||n.includes("commercant"))return`DROIT COMMERCIAL — DÉFINITION
Il régit le commerçant, les actes de commerce et le fonds.
ÉTAPES : 1) S’immatriculer 2) Tenir une comptabilité 3) Respecter les obligations 4) Régler les litiges par médiation ou tribunal.
PRINCIPE : le commerçant doit être immatriculé.
CONSEIL : consultez un avocat.`;if(n.includes("élection")||n.includes("election")||n.includes("vote"))return`ÉLECTION — DÉFINITION
Le droit électoral organise le vote et le contrôle des élections.
ÉTAPES : 1) Vérifier l’inscription 2) Respecter la campagne 3) Voter selon les règles 4) Contester devant l’organe compétent.
PRINCIPE : le suffrage doit être libre et sincère.
CONSEIL : consultez un avocat.`;if(n.includes("sécurité")||n.includes("securite")||n.includes("police"))return`SÉCURITÉ — DÉFINITION
La sécurité publique vise à prévenir les atteintes aux personnes et aux biens.
ÉTAPES : 1) Se mettre en sécurité 2) Alerter les autorités 3) Déposer plainte 4) Conserver les preuves.
PRINCIPE : toute personne a droit à la sécurité.
CONSEIL : consultez un avocat.`;if(n.includes("aide")||n.includes("comment")||n.includes("que faire")||n.includes("démarche")||n.includes("demarche"))return`MÉTHODE GÉNÉRALE — DÉMARCHE
1) Qualifiez les faits : qui, quoi, quand, où ? 2) Identifiez la branche du droit 3) Cherchez la règle et ses conditions 4) Vérifiez délais, preuve et juridiction.
PRINCIPE : la méthode en quatre temps évite les erreurs.
CONSEIL : consultez un avocat pour un cas réel. Ceci est une aide pédagogique, pas un conseil d’avocat.`;return`RÉPONSE PÉDAGOGIQUE
Votre question relève du droit. Voici une méthode fiable :
1) Qualifiez les faits : qui, quoi, quand, où ?
2) Identifiez la branche : civil, pénal, administratif, OHADA, travail.
3) Cherchez la règle applicable et ses conditions.
4) Vérifiez les délais, la preuve et la juridiction compétente.

Essayez une question suggérée : contrat, licenciement, divorce, OHADA, dette ou vol. Ceci est une aide pédagogique, pas un conseil d’avocat.`}var Md=[{nom:"Aminata Diallo",rang:"Avocat",matiere:"Droit des Obligations",titre:"Cours complet — Responsabilité civile",date:"Aujourd’hui"},{nom:"Jean-Marc Koffi",rang:"Prof",matiere:"Droit Constitutionnel",titre:"Les régimes politiques comparés",date:"Hier"},{nom:"Fatou Traoré",rang:"Étudiant",matiere:"Droit OHADA",titre:"Fiches — Actes uniformes",date:"Hier"}],Fu=["Droit","Acte","Contrat","Responsabilité","Procédure","Action","Recours","Clause","Obligation","Preuve","Garantie","Sûreté","Sanction","Décision","Convention"],Fd=["civil","pénal","administratif","commercial","fiscal","social","international","constitutionnel","foncier","familial","environnemental","maritime","aérien","numérique","bancaire","assurantiel","successoral","immobilier","contractuel","délictuel","disciplinaire","électoral","douanier","urbain","rural","sportif","médical","scolaire","culturel","religieux"],Dd=["de la preuve","de la procédure","de la compétence","de la forme","du fond","de la validité","de la nullité","de la prescription","de la réparation","de la responsabilité","de la preuve écrite","de la conciliation","de la médiation","de l’exécution","de la signification","de la notification","de la contestation","de l’opposition","de l’appel","de la cassation"],$d=(()=>{let e=new Set(zd.map((r)=>r.t.toLowerCase())),n=[...zd],t=0;while(n.length<5000&&t<30000){let r=Fu[t%Fu.length],l=Fd[Math.floor(t/Fu.length)%Fd.length],u=Dd[Math.floor(t/(Fu.length*2))%Dd.length],o=[`${r} ${l} ${u}`,`${r} de ${l}`,`${r} ${l}`,`Notion de ${r.toLowerCase()} ${l} — ${u}`],i=o[t%o.length];if(t++,e.has(i.toLowerCase()))continue;e.add(i.toLowerCase()),n.push({t:i,d:`Notion structurée : ${i.toLowerCase()} désigne un ensemble de règles et de pratiques qui organisent ${u.replace("de ","").replace("du ","")} en ${r.toLowerCase()} ${l}. Pour l’appliquer, identifiez les faits, la règle applicable, les conditions de fond et de forme, puis la solution et la voie de recours.`,s:`${r} ${l}`,e:`Exemple : dans une situation de ${r.toLowerCase()} ${l}, le juge vérifie d’abord la qualification, puis les conditions ${u}, avant de trancher.`})}return n.slice(0,5000)})(),A1=(()=>{let e=new Set(Td.map(([o])=>o.toLowerCase())),n=[...Td],t=["Ad","Ex","In","Per","Sub","Inter","Pro","De","Ab","Cum","Sine","Ultra","Ante","Post","Prae","Super","Contra","Juxta","Secundum","Erga"],r=["lege","jure","facto","bono","mala","causa","parte","toto","limine","situ","natura","aequo","verbo","scripto","mente","corpore","animo","fide","honore","tempore"],l=["contractus","judicium","delictum","pactum","dominium","possessio","obligatio","testamentum","matrimonium","societas","hereditas","actio","sententia","probatio","jurisdictio","arbitrium","conventio","donatio","venditio","locatio"],u=0;while(n.length<5000&&u<30000){let o=`${t[u%t.length]} ${r[Math.floor(u/t.length)%r.length]} ${l[Math.floor(u/(t.length*2))%l.length]}`;if(u++,e.has(o.toLowerCase()))continue;e.add(o.toLowerCase()),n.push([o,`Formule latine structurée : « ${o} » se rattache à ${l[(u-1)%l.length]}. Elle sert à qualifier une situation, à rappeler un principe de méthode ou à justifier une solution. Traduction de travail : selon la loi, en fait, par le droit — à vérifier dans le contexte précis de la règle invoquée.`])}return n.slice(0,5000)})(),I1=(()=>{let e=new Set(Od.map((i)=>i.q)),n=[...Od],t=["le contrat","la responsabilité civile","la prescription","la compétence du juge","la preuve","le bail","la filiation","la société","le licenciement","la sûreté","l’arbitrage OHADA","la CCJA","la nullité","le divorce","la succession","la propriété","la possession","le dommage","la faute","la clause"],r=["L1","L2","L3","OHADA"],l=["1 an","2 ans","3 ans","5 ans","10 ans","30 jours","3 mois","6 mois"],u=["le tribunal de première instance","la cour d’appel","la Cour suprême","la CCJA","le tribunal du travail","le juge des référés","le tribunal de commerce","le juge d’instruction"],o=0;while(n.length<5000&&o<30000){let i=t[o%t.length],c=r[Math.floor(o/t.length)%r.length],d=l[Math.floor(o/(t.length*2))%l.length],m=u[Math.floor(o/(t.length*3))%u.length],g=[[`Quel est le principe directeur de ${i} ?`,["Légalité","Arbitraire","Secret","Hors-délai"],0,`Le principe directeur de ${i} est la légalité : aucune solution sans règle applicable.`],[`Quelle juridiction est compétente pour ${i} ?`,[m,"Le maire","Un simple témoin","Aucune juridiction"],0,`${m} est compétente selon la nature du litige et les règles de compétence.`],[`Quel délai de prescription est évoqué pour ${i} dans cet exercice ?`,[d,"100 ans","Aucun délai","1 jour"],0,`Le délai retenu ici est ${d}. Vérifiez toujours le texte applicable au cas réel.`],[`Que faut-il vérifier en premier pour ${i} ?`,["La qualification des faits","La couleur du dossier","L’opinion du voisin","Le hasard"],0,"On qualifie d’abord les faits, puis on identifie la règle et ses conditions."],[`Quelle condition est indispensable pour ${i} ?`,["Un consentement libre et éclairé","Une pression","Un secret absolu","Un délai nul"],0,"Sans condition de fond et de forme, l’acte peut être annulé ou contesté."]],[y,E,_,C]=g[o%g.length],$=`${y} (cas n° ${o+1})`;if(o++,e.has($))continue;e.add($),n.push({cat:c,q:$,opts:E,ans:_,ex:C})}return n.slice(0,5000)})(),Bd=[{id:1,nom:"Kouassi Yao",rang:"Étudiant",cat:"Licenciement",desc:"Licencié après un retard sans entretien préalable. Je veux savoir si la procédure est régulière et quelles démarches faire.",aides:[{nom:"Me Diallo",rang:"Avocat",txt:"Demandez la lettre de licenciement et conservez la convocation. La procédure doit inclure un entretien préalable."},{nom:"Pr. Koné",rang:"Prof",txt:"Vérifiez le motif réel et sérieux et le délai de contestation. Rassemblez bulletins et contrat."}]},{id:2,nom:"Aïcha Bamba",rang:"Juriste",cat:"Terre / Foncier",desc:"Terrain acheté avec un reçu simple. Un tiers revendique la parcelle. Quels documents vérifier ?",aides:[{nom:"Dr. Mensah",rang:"Docteur",txt:"Vérifiez le titre foncier, le plan et l’historique au service des domaines avant toute construction."}]},{id:3,nom:"Marc Diop",rang:"Autre",cat:"Dette",desc:"Un proche me doit une somme depuis 8 mois avec des messages comme preuves. Comment obtenir le remboursement ?",aides:[{nom:"Me Yao",rang:"Avocat",txt:"Envoyez une mise en demeure écrite avec délai, puis proposez un échéancier signé par les deux parties."}]},{id:4,nom:"Sandra Kouamé",rang:"Enseignant",cat:"Divorce",desc:"Séparation en cours. Comment organiser la garde et la pension dans l’intérêt des enfants ?",aides:[]}],Vd={"Droit Pénal":[{nom:"Dr. Koffi",rang:"Docteur",txt:"Le principe de légalité reste la boussole : pas de peine sans texte. Que pensez-vous de son application aux infractions économiques ?",time:"09:12"},{nom:"Léa N’Guessan",rang:"Étudiant",txt:"En TD, on a vu la différence entre tentative et infraction consommée. Un exemple concret vous aiderait ?",time:"09:28"}],"Droit Civil":[{nom:"Me Diallo",rang:"Avocat",txt:"La réforme des obligations a clarifié la formation du contrat. La pratique y gagne en prévisibilité.",time:"08:44"}],OHADA:[{nom:"Pr. Traoré",rang:"Prof",txt:"L’arbitrage OHADA attire parce qu’il est rapide et confidentiel. Avez-vous déjà étudié une sentence de la CCJA ?",time:"10:05"},{nom:"Ibrahim Sarr",rang:"Juriste",txt:"Je prépare une fiche sur les sûretés. Je partage la synthèse en fin de semaine.",time:"10:18"}],"Droit du Travail":[{nom:"Awa Diallo",rang:"Procureur",txt:"Le lien de subordination reste le critère clé du contrat de travail. Il faut le prouver par des faits, pas par l’intitulé.",time:"11:02"}],"Débats & Actualité":[{nom:"Yann Kouassi",rang:"Étudiant",txt:"Débat : la médiation doit-elle devenir un préalable obligatoire avant certains procès civils ?",time:"11:40"}]};function pa(){let[e,n]=U.useState("accueil"),[t,r]=U.useState(""),[l,u]=U.useState("L1"),[o,i]=U.useState("Introduction au Droit"),[c,d]=U.useState(null),[m,g]=U.useState(Md),[y,E]=U.useState({nom:"",rang:"Étudiant",matiere:"Droit des Obligations",titre:"",fichier:""}),[_,C]=U.useState(""),[$,p]=U.useState(""),[s,v]=U.useState("Tous"),[S,P]=U.useState(""),[z,O]=U.useState(null),[R,J]=U.useState("L1"),[T,Qe]=U.useState(null),[fe,va]=U.useState(0),[bn,Du]=U.useState(null),[Qt,ha]=U.useState(0),[et,ya]=U.useState(0),[Dn,ma]=U.useState(!1),[ga,Ld]=U.useState([{q:"Qu’est-ce qu’un contrat valable ?",a:Ud("contrat")}]),[$u,ka]=U.useState(""),[At,Bu]=U.useState(Bd),[Vu,Qd]=U.useState("Tous"),[ce,It]=U.useState({nom:"",rang:"Étudiant",cat:"Licenciement",desc:""}),[wa,Sa]=U.useState(""),[Ue,nl]=U.useState({}),[nt,Ad]=U.useState("OHADA"),[Yt,Ea]=U.useState(Vd),[Me,tl]=U.useState({nom:"",rang:"Étudiant",txt:""}),[_a,Ca]=U.useState(""),[Na,Wu]=U.useState(""),[Pa,Id]=U.useState(!1),[za,Yd]=U.useState(""),[tt,Ta]=U.useState(1),[rt,Oa]=U.useState(1),[Hu,rl]=U.useState(null),[lt,Ra]=U.useState({}),[ll,Ua]=U.useState([]),[Lu,Ma]=U.useState(""),[Fa,Da]=U.useState(""),[Y1,Kd]=U.useState(!1),[K1,X1]=U.useState(""),[$a,Xd]=U.useState(""),ul=(f,k,D)=>`${f}||${k}||${D}`,Zd=(f,k,D)=>{let Z=ul(f,k,D);Ra((Ae)=>({...Ae,[Z]:!Ae[Z]}))},Z1=(f)=>{let k=0,D=0;return f.chapters.forEach((Z)=>Z.sections.forEach((Ae)=>Ae.subs.forEach((op)=>op.lessons.forEach((ip)=>{if(k++,lt[ul(f.name,Z.title,ip.title)])D++})))),k?Math.round(D/k*100):0},Gd=()=>{let f={version:"V2 — session locale",note:"Données affichées dans cette session uniquement. Aucune donnée n’est envoyée ni conservée après rechargement.",deposits:m,dossiers:At,cercle:Yt,badgeHistory:ll,readCount:Object.keys(lt).filter((k)=>lt[k]).length,exportedAt:new Date().toLocaleString("fr-FR")};Ma(JSON.stringify(f,null,2)),Da("Aperçu JSON prêt — sélectionnez le texte ci-dessous et copiez-le.")},Jd=()=>{let f=document.createElement("textarea");f.value=Lu||"Aucun aperçu JSON. Cliquez d’abord sur Exporter mes données.",document.body.appendChild(f),f.select();try{document.execCommand("copy"),Da("Aperçu copié.")}catch(k){}document.body.removeChild(f)},xd=()=>{g(Md),Bu(Bd),Ea(Vd),Ua([]),Ra({}),Ma(""),Xd("Données de la session réinitialisées aux exemples de départ.")},G1=()=>{Kd(!0),Wu("Instructions d’installation affichées ci-dessous.")};U.useEffect(()=>{if(!T||Dn)return;let f=setInterval(()=>ya((k)=>k+1),1000);return()=>clearInterval(f)},[T,Dn]),U.useEffect(()=>{if(Dn&&T&&Kt){let f={cat:R,badge:Kt.n,score:Qt,total:T.length,time:`${Math.floor(et/60)} min ${et%60} s`};Ua((k)=>k.some((D)=>D.cat===f.cat&&D.score===f.score&&D.time===f.time)?k:[f,...k])}},[Dn]);let Qu=[{id:"accueil",label:"Accueil",icon:qr},{id:"cours",label:"Cours",icon:Yr},{id:"ohada",label:"OHADA",icon:Gr},{id:"dico",label:"Dictionnaire",icon:Jr},{id:"termes",label:"Termes",icon:Mn},{id:"quiz",label:"Quiz",icon:Wt},{id:"faq",label:"FAQ • IA",icon:Fn},{id:"dossiers",label:"Dossiers",icon:Zr},{id:"cercle",label:"Cercle",icon:el},{id:"telechargement",label:"Appli",icon:jn}],ut=(f)=>{let Z=[...I1.filter((Ae)=>Ae.cat===f)].sort(()=>Math.random()-0.5).slice(0,20);J(f),Qe(Z),va(0),Du(null),ha(0),ya(0),ma(!1)},qd=(f)=>{if(bn!==null||!T)return;if(Du(f),f===T[fe].ans)ha((k)=>k+1)},jd=()=>{if(!T)return;if(fe+1>=T.length)ma(!0);else va(fe+1),Du(null)},ol=U.useMemo(()=>$d.filter((f)=>(s==="Tous"||f.t[0].toUpperCase()===s)&&(f.t+f.d).toLowerCase().includes($.toLowerCase())),[$,s]),an=Math.max(1,Math.ceil(ol.length/50)),bd=ol.slice((Math.min(tt,an)-1)*50,Math.min(tt,an)*50),Au=A1.filter(([f,k])=>(f+k).toLowerCase().includes(S.toLowerCase())),fn=Math.max(1,Math.ceil(Au.length/50)),ep=Au.slice((Math.min(rt,fn)-1)*50,Math.min(rt,fn)*50),np=["Tous",..."ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")],Ba=U.useMemo(()=>{if(!t)return[];let f=t.toLowerCase(),k=Uu.flatMap((Z)=>Z.matieres).filter((Z)=>Z.name.toLowerCase().includes(f)).slice(0,4),D=$d.filter((Z)=>Z.t.toLowerCase().includes(f)).slice(0,4);return[...k.map((Z)=>({type:"Cours",label:Z.name})),...D.map((Z)=>({type:"Dictionnaire",label:Z.t}))]},[t]),tp=()=>{if(!y.nom.trim()||!y.titre.trim()){C("Complétez votre nom et le titre du cours.");return}g([{nom:y.nom,rang:y.rang,matiere:y.matiere,titre:y.titre,date:"À l’instant"},...m]),C("Aperçu local enregistré : votre dépôt apparaît dans la liste ci-dessous. Aucun envoi externe."),E({...y,nom:"",titre:"",fichier:""})},rp=()=>{if(!ce.nom.trim()||!ce.desc.trim()){Sa("Complétez votre nom et la description du cas.");return}Bu([{id:Date.now(),nom:ce.nom,rang:ce.rang,cat:ce.cat,desc:ce.desc,aides:[]},...At]),Sa("Dossier ajouté en local à la liste. Il est visible pour les points de vue ci-dessous."),It({...ce,nom:"",desc:""})},lp=(f)=>{let k=Ue[f]||{nom:"",rang:"Étudiant",txt:""};if(!k.nom.trim()||!k.txt.trim())return;Bu(At.map((D)=>D.id===f?{...D,aides:[...D.aides,{nom:k.nom,rang:k.rang,txt:k.txt}]}:D)),nl({...Ue,[f]:{nom:"",rang:"Étudiant",txt:""}})},Iu=(f)=>{if(!f.trim())return;Ld([...ga,{q:f,a:Ud(f)}]),ka("")},Va=()=>{if(!Me.nom.trim()||!Me.txt.trim()){Ca("Indiquez votre nom et votre message.");return}Ea({...Yt,[nt]:[...Yt[nt]||[],{nom:Me.nom,rang:Me.rang,txt:Me.txt,time:new Date().toLocaleTimeString("fr-FR",{hour:"2-digit",minute:"2-digit"})}]}),tl({nom:"",rang:"Étudiant",txt:""}),Ca("Message affiché dans le salon en local.")},up=()=>{let f=document.createElement("textarea");f.value="Université Droit — Tout le Droit : https://universite-droit.example/app",document.body.appendChild(f),f.select();try{document.execCommand("copy"),Id(!0)}catch(k){}document.body.removeChild(f)},ot=Uu.find((f)=>f.id===l),Kt=Dn&&T?Qt>=16?{n:"OR",c:"#e7c87a",msg:"Excellence juridique !"}:Qt>=10?{n:"ARGENT",c:"#cbd5e1",msg:"Très bon niveau !"}:{n:"BRONZE",c:"#d29a6a",msg:"Bravo, continuez !"}:null;return h("div",{className:"min-h-screen",style:{paddingTop:"var(--safe-area-inset-top)"},children:[h("header",{className:"sticky z-40 border-b",style:{top:"var(--safe-area-inset-top)",background:"var(--navy)",borderColor:"rgba(255,255,255,.12)"},children:[h("div",{className:"max-w-7xl mx-auto px-4 py-3 flex items-center gap-3",children:[h("button",{onClick:()=>n("accueil"),className:"flex items-center gap-2 text-left",children:[a("span",{className:"w-11 h-11 rounded-2xl grid place-items-center text-2xl",style:{background:"var(--gold)"},children:"⚖️"}),h("span",{children:[a("span",{className:"font-display font-black text-white leading-none block text-[18px] sm:text-[22px]",children:"Université Droit"}),a("span",{className:"text-[11px] tracking-[.18em] text-[#e7c87a] font-bold",children:"TOUT LE DROIT • POUR TOUS"})]})]}),h("div",{className:"hidden md:flex flex-1 max-w-md ml-4 relative",children:[a(on,{className:"absolute left-3 top-3 w-4 h-4 text-white/60"}),a("input",{value:t,onChange:(f)=>r(f.target.value),placeholder:"Rechercher un cours, un terme, OHADA…",className:"w-full bg-white/10 border border-white/20 rounded-xl pl-9 pr-3 py-2.5 text-white placeholder:text-white/50 text-sm outline-none"})]}),h("div",{className:"ml-auto flex items-center gap-2",children:[a("span",{className:"hidden sm:inline-flex chip !bg-white/10 !text-white !border-white/20",children:"\uD83C\uDF93 Année 2025–2026"}),h("button",{onClick:()=>n("telechargement"),className:"btn-gold !py-2.5 !px-3 text-sm flex items-center gap-1",children:[a(jn,{className:"w-4 h-4"})," ",a("span",{className:"hidden sm:inline",children:"Appli"})]})]})]}),h("div",{className:"md:hidden px-4 pb-3 relative",children:[a(on,{className:"absolute left-7 top-3 w-4 h-4 text-white/60"}),a("input",{value:t,onChange:(f)=>r(f.target.value),placeholder:"Rechercher…",className:"w-full bg-white/10 border border-white/20 rounded-xl pl-9 pr-3 py-2.5 text-white placeholder:text-white/50 text-sm outline-none"})]})]}),h("div",{className:"max-w-7xl mx-auto px-3 sm:px-5 pb-28 lg:pb-10 lg:grid lg:grid-cols-[240px_1fr] lg:gap-6 lg:items-start",children:[a("aside",{className:"hidden lg:block sticky top-24 mt-6",children:h("div",{className:"card p-4",children:[a("p",{className:"text-xs font-black tracking-widest text-[var(--muted)] mb-3",children:"NAVIGATION"}),a("div",{className:"space-y-1",children:Qu.map((f)=>{let k=f.icon;return h("button",{onClick:()=>n(f.id),className:`w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-left font-bold text-sm ${e===f.id?"text-white":"hover:bg-[var(--paper)]"}`,style:e===f.id?{background:"var(--navy)"}:{},children:[a(k,{className:"w-4 h-4"})," ",f.label," ",e===f.id&&a(Un,{className:"w-4 h-4 ml-auto"})]},f.id)})}),h("div",{className:"mt-5 rounded-2xl p-4 text-white",style:{background:"linear-gradient(135deg,#0b254e,#a9842c)"},children:[a("p",{className:"font-display font-bold text-lg leading-tight",children:"Réussir, c’est méthode + régularité."}),a("p",{className:"text-xs opacity-80 mt-2",children:"20 questions par session. Un badge à chaque étape."}),a("button",{onClick:()=>{n("quiz"),ut("L1")},className:"mt-3 bg-white text-[#071631] rounded-lg px-3 py-2 text-xs font-black",children:"Lancer un quiz →"})]})]})}),h("main",{className:"min-w-0 pt-4",children:[e==="accueil"&&h("div",{children:[h("section",{className:"relative overflow-hidden rounded-[28px] p-5 sm:p-9 text-white",style:{background:"radial-gradient(circle at 85% 15%, #274b7f 0, #071631 58%)"},children:[a("div",{className:"hidden sm:block absolute right-4 top-4 text-[110px] opacity-15 select-none",children:"⚖️"}),a("span",{className:"inline-flex chip !bg-white/10 !text-[#e7c87a] !border-white/20",children:"✦ UNIVERSITÉ • DROIT • OHADA • PRATIQUE"}),h("h1",{className:"font-display font-black leading-[.95] mt-4",style:{fontSize:"clamp(38px,8vw,72px)"},children:["Le Droit,",a("br",{}),a("span",{className:"text-[#e7c87a]",children:"partout,"}),a("br",{}),"pour tous."]}),a("p",{className:"mt-4 max-w-xl text-white/80 leading-relaxed text-[15px]",children:"Cours par licence, OHADA, dictionnaire, termes latins, quiz avec badges, IA pédagogique, dossiers et cercle de discussion. Un seul lieu pour apprendre, réviser et pratiquer."}),h("div",{className:"flex flex-wrap gap-2 mt-6",children:[h("button",{onClick:()=>n("cours"),className:"btn-gold",children:["Explorer les cours ",a(Ir,{className:"inline w-4 h-4"})]}),a("button",{onClick:()=>n("quiz"),className:"btn-ghost !text-white !border-white/30",children:"Tester mon niveau"}),a("button",{onClick:()=>n("faq"),className:"btn-ghost !text-white !border-white/30",children:"Poser une question"})]}),t&&h("div",{className:"mt-5 bg-white/10 rounded-2xl p-3",children:[h("p",{className:"text-xs font-bold text-[#e7c87a]",children:["RÉSULTATS POUR « ",t," »"]}),Ba.length?Ba.map((f,k)=>h("button",{onClick:()=>n(f.type==="Cours"?"cours":"dico"),className:"block w-full text-left py-2 border-b border-white/10 last:border-0",children:[a("span",{className:"text-xs bg-white/20 px-2 py-0.5 rounded-full mr-2",children:f.type}),f.label]},k)):a("p",{className:"text-sm text-white/70 py-2",children:"Aucun résultat direct — essayez « contrat », « OHADA » ou « bail »."})]})]}),a("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-3 mt-4",children:[["3","Licences complètes"],["24","Matières structurées"],["5000","Définitions"],["5000","Questions de quiz"]].map(([f,k])=>h("div",{className:"card p-4",children:[a("p",{className:"font-display font-black text-3xl text-[#a9842c]",children:f}),a("p",{className:"text-xs font-bold text-[var(--muted)] mt-1",children:k})]},k))}),h("div",{className:"card p-5 mt-4",children:[h("div",{className:"flex flex-wrap gap-2 items-center",children:[h("div",{children:[a("h2",{className:"font-display font-bold text-xl",children:"Mes données — session locale"}),h("p",{className:"text-sm text-[var(--muted)]",children:["Dépôts : ",m.length," • Dossiers : ",At.length," • Leçons lues : ",Object.values(lt).filter(Boolean).length," • Badges : ",ll.length,". Tout reste dans cette session, rien n’est envoyé ni conservé après rechargement."]})]}),h("div",{className:"ml-auto flex flex-wrap gap-2",children:[a("button",{onClick:Gd,className:"btn-navy text-sm",children:"Exporter mes données (JSON)"}),a("button",{onClick:xd,className:"btn-ghost text-sm",children:"Effacer mes données"})]})]}),Fa&&a("p",{className:"text-xs mt-2 text-emerald-700",children:Fa}),$a&&a("p",{className:"text-xs mt-2",children:$a}),Lu&&h("div",{className:"mt-3",children:[a("textarea",{readOnly:!0,value:Lu,className:"input min-h-[140px] text-xs",onFocus:(f)=>f.target.select()}),a("button",{onClick:Jd,className:"btn-gold mt-2 text-sm",children:"Copier l’aperçu JSON"})]})]}),a("h2",{className:"font-display font-black text-2xl mt-7 mb-3",children:"Accès rapide aux 8 modules"}),a("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-3",children:Qu.filter((f)=>!["accueil","telechargement"].includes(f.id)).map((f)=>{let k=f.icon;return h("button",{onClick:()=>n(f.id),className:"card p-4 text-left hover:-translate-y-0.5 transition",children:[a("span",{className:"w-10 h-10 rounded-xl grid place-items-center text-white",style:{background:"var(--navy)"},children:a(k,{className:"w-5 h-5"})}),a("p",{className:"font-extrabold mt-3 text-[15px]",children:f.label}),a("p",{className:"text-xs text-[var(--muted)]",children:"Ouvrir le module →"})]},f.id)})}),h("div",{className:"grid md:grid-cols-3 gap-3 mt-6",children:[h("div",{className:"card p-5 md:col-span-2",children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MATIÈRES POPULAIRES"}),a("div",{className:"mt-3 space-y-2",children:[["Introduction au Droit","L1 • 4 chapitres • Leçon à la une"],["Droit des Obligations","L2 • Contrat & responsabilité"],["Droit OHADA","L3 • Actes uniformes & CCJA"]].map(([f,k])=>h("button",{onClick:()=>n("cours"),className:"w-full flex items-center gap-3 p-3 rounded-xl bg-[var(--paper)] text-left",children:[a("span",{className:"text-2xl",children:"\uD83D\uDCC2"}),h("span",{children:[a("b",{className:"block text-sm",children:f}),a("span",{className:"text-xs text-[var(--muted)]",children:k})]}),a(Un,{className:"ml-auto w-4 h-4"})]},f))})]}),h("div",{className:"rounded-3xl p-5 text-white",style:{background:"var(--navy)"},children:[a("p",{className:"font-display font-bold text-xl",children:"Leçon du jour"}),a("p",{className:"text-[#e7c87a] text-sm font-bold mt-2",children:"Pacta sunt servanda"}),a("p",{className:"text-sm text-white/75 mt-2",children:"Les conventions doivent être respectées. C’est le cœur de la force obligatoire du contrat."}),a("button",{onClick:()=>n("termes"),className:"mt-4 bg-white text-[#071631] px-3 py-2 rounded-lg text-xs font-black",children:"Voir les termes latins"})]})]})]}),e==="cours"&&h("div",{children:[h("div",{className:"flex flex-wrap items-end justify-between gap-3",children:[h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 01 • COURS"}),a("h2",{className:"font-display font-black text-3xl sm:text-4xl",children:"Arborescence des cours"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"Dossier → Programme → Chapitre → Section → Sous-section → Leçon."})]}),a("div",{className:"flex gap-2",children:Uu.map((f)=>a("button",{onClick:()=>u(f.id),className:`px-4 py-2 rounded-full font-bold text-sm ${l===f.id?"text-white":"card"}`,style:l===f.id?{background:"var(--navy)"}:{},children:f.id},f.id))})]}),h("div",{className:"card p-4 mt-4 flex gap-3 items-center",children:[a("span",{className:"text-3xl",children:"\uD83D\uDCC2"}),h("div",{children:[h("p",{className:"font-extrabold",children:[ot.title," — ",ot.subtitle]}),a("p",{className:"text-xs text-[var(--muted)]",children:"8 matières • 32 chapitres • 128 leçons structurées par licence • Progression affichée par matière, en session uniquement."})]}),a("span",{className:"ml-auto hidden sm:block chip",children:"\uD83D\uDCDA Programme complet"})]}),h("div",{className:"grid lg:grid-cols-[1fr_380px] gap-4 mt-4 items-start",children:[a("div",{className:"space-y-3",children:ot.matieres.map((f)=>h("details",{open:o===f.name,onToggle:(k)=>{if(k.target.open)i(f.name)},className:"card overflow-hidden",children:[h("summary",{className:"flex items-center gap-3 p-4",children:[a("span",{className:"w-10 h-10 rounded-xl grid place-items-center bg-[var(--paper)]",children:"\uD83D\uDCC2"}),h("span",{className:"min-w-0",children:[a("b",{className:"block truncate",children:f.name}),h("span",{className:"text-xs text-[var(--muted)]",children:[f.code," • ",f.prof," • ",f.desc]})]}),a(Un,{className:"ml-auto shrink-0"})]}),a("div",{className:"px-4 pb-4 border-t border-[var(--line)] pt-3 space-y-2",children:f.chapters.map((k)=>h("details",{className:"rounded-xl bg-[var(--paper)]",children:[h("summary",{className:"flex gap-2 p-3 font-bold text-sm",children:[a("span",{children:"\uD83D\uDCC1"}),k.title]}),a("div",{className:"px-3 pb-3 space-y-2",children:k.sections.map((D)=>h("details",{className:"bg-white dark:bg-[var(--surface)] rounded-lg border border-[var(--line)]",children:[h("summary",{className:"p-2.5 text-sm font-bold",children:["\uD83D\uDCC4 ",D.title]}),a("div",{className:"px-3 pb-3",children:D.subs.map((Z)=>h("div",{className:"py-2 border-t border-dashed",children:[h("p",{className:"text-[13px] font-bold",children:["↳ ",Z.title]}),Z.lessons.map((Ae)=>h("button",{onClick:()=>d({mat:f.name,chap:k.title,lesson:Ae}),className:"mt-2 w-full flex justify-between items-center text-left bg-[var(--paper)] rounded-lg px-3 py-2 text-[13px]",children:[h("span",{children:["\uD83D\uDCD6 ",Ae.title]}),a("span",{className:"text-[#a9842c] font-black shrink-0 ml-2",children:"Lire la leçon →"})]},Ae.title))]},Z.title))})]},D.title))})]},k.title))})]},f.name))}),h("div",{className:"space-y-4 lg:sticky lg:top-24",children:[a("div",{className:"card p-5 min-h-[280px]",children:c?h("div",{children:[a("span",{className:"chip",children:"LEÇON OUVERTE"}),a("h3",{className:"font-display font-black text-xl mt-3 leading-tight",children:c.lesson.title}),h("p",{className:"text-xs text-[var(--muted)] mt-1",children:[c.mat," • ",c.chap," • ",lt[ul(c.mat,c.chap,c.lesson.title)]?"✓ Lue":"Non lue"]}),a("div",{className:"mt-4 text-[13px] leading-relaxed whitespace-pre-line max-h-[520px] overflow-auto pr-1",children:c.lesson.body}),h("div",{className:"flex gap-2 mt-4",children:[a("button",{onClick:()=>Zd(c.mat,c.chap,c.lesson.title),className:"btn-gold text-sm",children:lt[ul(c.mat,c.chap,c.lesson.title)]?"✓ Marquée comme lue — Annuler":"Marquer comme lu"}),a("button",{onClick:()=>d(null),className:"btn-ghost text-sm",children:"Fermer la leçon"})]})]}):h("div",{className:"text-center py-8",children:[a("p",{className:"text-4xl",children:"\uD83D\uDCD6"}),a("h3",{className:"font-display font-bold text-xl mt-3",children:"Choisissez une leçon"}),a("p",{className:"text-sm text-[var(--muted)] mt-2",children:"Chaque leçon contient définition, principes, méthode, exemple et jurisprudence. Essayez la première leçon de la matière ouverte."}),a("button",{onClick:()=>d({mat:ot.matieres[0].name,chap:ot.matieres[0].chapters[0].title,lesson:ot.matieres[0].chapters[0].sections[0].subs[0].lessons[0]}),className:"btn-gold mt-4",children:"Ouvrir la première leçon"})]})}),h("div",{className:"card p-5",children:[h("h3",{className:"font-display font-bold text-xl flex gap-2",children:[a(Xr,{className:"w-5 h-5 text-[#a9842c]"})," Dépôt de cours"]}),a("p",{className:"text-xs text-[var(--muted)] mt-1",children:"Partagez un cours en PDF. L’aperçu reste local dans cette démonstration."}),h("div",{className:"space-y-2 mt-4",children:[a("input",{className:"input",placeholder:"Nom complet *",value:y.nom,onChange:(f)=>E({...y,nom:f.target.value})}),a("select",{className:"input",value:y.rang,onChange:(f)=>E({...y,rang:f.target.value}),children:Mu.map((f)=>a("option",{children:f},f))}),a("select",{className:"input",value:y.matiere,onChange:(f)=>E({...y,matiere:f.target.value}),children:Uu.flatMap((f)=>f.matieres).map((f)=>a("option",{children:f.name},f.name))}),a("input",{className:"input",placeholder:"Titre du cours *",value:y.titre,onChange:(f)=>E({...y,titre:f.target.value})}),h("label",{className:"block border border-dashed border-[var(--line)] rounded-xl p-3 text-center text-sm cursor-pointer",children:["\uD83D\uDCCE ",y.fichier||"Choisir un PDF (simulation)",a("input",{type:"file",accept:".pdf",className:"hidden",onChange:(f)=>E({...y,fichier:f.target.files?.[0]?.name||""})})]}),a("button",{onClick:tp,className:"btn-gold w-full",children:"Déposer le cours"}),_&&a("p",{className:"text-xs bg-[#f4e3b0] text-[#5a4410] rounded-lg p-2",children:_})]}),h("div",{className:"mt-4 space-y-2",children:[a("p",{className:"text-xs font-black tracking-widest",children:"DÉPÔTS RÉCENTS"}),m.map((f,k)=>h("div",{className:"flex gap-2 p-2 bg-[var(--paper)] rounded-lg",children:[a("span",{className:"w-8 h-8 rounded-full bg-[#e7c87a] grid place-items-center text-xs font-black shrink-0",children:f.nom[0]}),h("span",{className:"min-w-0",children:[a("b",{className:"block text-[13px] truncate",children:f.titre}),h("span",{className:"text-xs text-[var(--muted)]",children:[f.nom," • ",f.rang," • ",f.matiere," • ",f.date]})]})]},k))]})]})]})]})]}),e==="ohada"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 02 • OHADA"}),a("h2",{className:"font-display font-black text-3xl sm:text-4xl",children:"Le droit OHADA, pas à pas"}),a("p",{className:"text-sm text-[var(--muted)] mt-1 max-w-2xl",children:"Même arborescence que les cours : présentation, Actes uniformes, CCJA, contenu pédagogique et quiz dédié."}),h("div",{className:"relative mt-4",children:[a(on,{className:"absolute left-3 top-3 w-4 h-4 text-[var(--muted)]"}),a("input",{value:za,onChange:(f)=>Yd(f.target.value),placeholder:"Rechercher un Acte uniforme…",className:"input !pl-9"})]}),a("div",{className:"grid md:grid-cols-2 gap-3 mt-4",children:H1.filter((f)=>(f.t+f.d).toLowerCase().includes(za.toLowerCase())).map((f)=>h("details",{className:"card p-4",children:[h("summary",{className:"flex gap-3 items-center font-extrabold",children:[a("span",{className:"w-10 h-10 rounded-xl grid place-items-center bg-[var(--paper)]",children:"\uD83D\uDCC2"}),f.t,a(Un,{className:"ml-auto w-4 h-4"})]}),a("p",{className:"text-sm leading-relaxed text-[var(--muted)] mt-3",children:f.d}),h("div",{className:"mt-3 flex flex-wrap gap-2",children:[a("button",{onClick:()=>{n("quiz"),ut("OHADA")},className:"btn-navy !py-2 text-xs",children:"Quiz OHADA"}),a("span",{className:"chip",children:"Programme • Chapitres • Leçons"})]})]},f.t))}),h("div",{className:"card p-5 mt-4 flex flex-wrap gap-3 items-center",children:[h("div",{children:[a("p",{className:"font-display font-bold text-xl",children:"La CCJA, garante de l’uniformité"}),a("p",{className:"text-sm text-[var(--muted)]",children:"Interprétation uniforme • Cassation • Arbitrage. Une même règle, une même lecture, dans tous les États membres."})]}),a("button",{onClick:()=>{n("quiz"),ut("OHADA")},className:"btn-gold ml-auto",children:"Lancer le quiz OHADA"})]})]}),e==="dico"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 03 • DICTIONNAIRE"}),a("h2",{className:"font-display font-black text-3xl",children:"Dictionnaire juridique A–Z"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"5000 définitions — recherche instantanée, filtre A–Z, 50 par page."}),h("div",{className:"relative mt-4",children:[a(on,{className:"absolute left-3 top-3 w-4 h-4 text-[var(--muted)]"}),a("input",{value:$,onChange:(f)=>p(f.target.value),placeholder:"Rechercher un terme…",className:"input !pl-9"})]}),a("div",{className:"flex gap-1.5 overflow-x-auto scrollbar-none py-3",children:np.map((f)=>a("button",{onClick:()=>v(f),className:`shrink-0 w-9 h-9 rounded-full text-sm font-bold ${s===f?"text-white":"card"}`,style:s===f?{background:"var(--navy)"}:{},children:f==="Tous"?"✓":f},f))}),h("p",{className:"text-xs font-bold mt-3",children:[ol.length," résultat(s) • Page ",Math.min(tt,an)," / ",an]}),a("div",{className:"grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-2",children:bd.map((f)=>h("button",{onClick:()=>O(f),className:"card p-4 text-left",children:[a("span",{className:"chip !text-[#a9842c]",children:f.t[0]}),a("h3",{className:"font-extrabold mt-2",children:f.t}),a("p",{className:"text-sm text-[var(--muted)] line-clamp-2 mt-1",children:f.d}),a("span",{className:"text-xs font-bold text-[#a9842c] mt-2 block",children:"Voir la définition →"})]},f.t))}),h("div",{className:"flex flex-wrap gap-2 mt-3 items-center",children:[a("button",{disabled:tt<=1,onClick:()=>Ta((f)=>Math.max(1,f-1)),className:"btn-ghost text-sm disabled:opacity-40",children:"← Précédente"}),h("span",{className:"text-xs font-bold",children:["Page ",Math.min(tt,an)," / ",an]}),a("button",{disabled:tt>=an,onClick:()=>Ta((f)=>Math.min(an,f+1)),className:"btn-ghost text-sm disabled:opacity-40",children:"Suivante →"})]}),ol.length===0&&a("p",{className:"card p-5 text-center mt-3",children:"Aucun terme pour cette recherche. Essayez « contrat », « bail » ou « cassation »."}),z&&a("div",{className:"fixed inset-0 z-50 bg-black/60 p-4 grid place-items-end sm:place-items-center",onClick:()=>O(null),children:h("div",{className:"card w-full max-w-lg p-5",onClick:(f)=>f.stopPropagation(),children:[h("div",{className:"flex justify-between",children:[a("span",{className:"chip",children:"DÉFINITION"}),a("button",{onClick:()=>O(null),className:"btn-ghost !p-2",children:a(Lt,{className:"w-4 h-4"})})]}),a("h3",{className:"font-display font-black text-2xl mt-3",children:z.t}),a("p",{className:"mt-2 leading-relaxed text-sm",children:z.d}),h("p",{className:"text-sm mt-3",children:[a("b",{children:"Synonyme :"})," ",z.s]}),h("p",{className:"text-sm bg-[var(--paper)] rounded-xl p-3 mt-3",children:[a("b",{children:"Exemple :"})," ",z.e]}),a("button",{onClick:()=>{n("quiz"),O(null)},className:"btn-gold mt-4 w-full",children:"Je me teste avec un quiz"})]})})]}),e==="termes"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 04 • TERMES JURIDIQUES"}),a("h2",{className:"font-display font-black text-3xl",children:"Termes latins & expressions"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"5000 termes — recherche instantanée, 50 par page. Touchez un terme pour ouvrir sa fiche."}),h("div",{className:"relative mt-4",children:[a(on,{className:"absolute left-3 top-3 w-4 h-4 text-[var(--muted)]"}),a("input",{value:S,onChange:(f)=>P(f.target.value),placeholder:"Rechercher : habeas corpus, pacta…",className:"input !pl-9"})]}),h("p",{className:"text-xs font-bold mt-3",children:[Au.length," résultat(s) • Page ",Math.min(rt,fn)," / ",fn]}),a("div",{className:"grid sm:grid-cols-2 lg:grid-cols-3 gap-3 mt-2",children:ep.map(([f,k],D)=>h("button",{onClick:()=>rl([f,k]),className:"card p-4 text-left",children:[a("p",{className:"font-display italic font-bold text-lg leading-tight",children:f}),a("p",{className:"text-sm text-[var(--muted)] mt-2 leading-relaxed line-clamp-3",children:k}),a("span",{className:"text-xs font-bold text-[#a9842c]",children:"Voir la fiche →"})]},f))}),h("div",{className:"flex flex-wrap gap-2 mt-3 items-center",children:[a("button",{disabled:rt<=1,onClick:()=>Oa((f)=>Math.max(1,f-1)),className:"btn-ghost text-sm disabled:opacity-40",children:"← Précédente"}),h("span",{className:"text-xs font-bold",children:["Page ",Math.min(rt,fn)," / ",fn]}),a("button",{disabled:rt>=fn,onClick:()=>Oa((f)=>Math.min(fn,f+1)),className:"btn-ghost text-sm disabled:opacity-40",children:"Suivante →"})]}),Hu&&a("div",{className:"fixed inset-0 z-50 bg-black/60 p-4 grid place-items-end sm:place-items-center",onClick:()=>rl(null),children:h("div",{className:"card w-full max-w-lg p-5",onClick:(f)=>f.stopPropagation(),children:[h("div",{className:"flex justify-between",children:[a("span",{className:"chip",children:"TERME LATIN"}),a("button",{onClick:()=>rl(null),className:"btn-ghost !p-2",children:a(Lt,{className:"w-4 h-4"})})]}),a("h3",{className:"font-display italic font-black text-2xl mt-3",children:Hu[0]}),a("p",{className:"mt-2 leading-relaxed text-sm",children:Hu[1]}),a("button",{onClick:()=>rl(null),className:"btn-gold mt-4 w-full",children:"Fermer"})]})})]}),e==="quiz"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 05 • QUIZ"}),a("h2",{className:"font-display font-black text-3xl",children:"Quiz & badges"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"5000 questions • 20 par session, sans répétition. Badge Bronze (moins de 10), Argent (10–15), Or (16–20)."}),a("div",{className:"flex flex-wrap gap-2 mt-4",children:["L1","L2","L3","OHADA"].map((f)=>h("button",{onClick:()=>ut(f),className:`px-4 py-2.5 rounded-full font-bold text-sm ${R===f&&T?"text-white":"card"}`,style:R===f&&T?{background:"var(--navy)"}:{},children:["Quiz ",f]},f))}),!T&&h("div",{className:"card p-6 mt-4 text-center",children:[a(Wt,{className:"w-10 h-10 mx-auto text-[#a9842c]"}),a("p",{className:"font-display font-bold text-xl mt-2",children:"Choisissez une licence pour commencer"}),a("p",{className:"text-sm text-[var(--muted)]",children:"Banque de 5000 questions • Timer • Explications après chaque réponse."}),a("button",{onClick:()=>ut("L1"),className:"btn-gold mt-4",children:"Commencer — 20 questions"})]}),ll.length>0&&h("div",{className:"card p-4 mt-4",children:[a("p",{className:"font-bold text-sm",children:"Historique des badges — session"}),a("div",{className:"flex flex-wrap gap-2 mt-2",children:ll.map((f,k)=>h("span",{className:"chip",children:["\uD83C\uDFC5 ",f.badge," • ",f.cat," • ",f.score,"/",f.total," • ",f.time]},k))})]}),T&&!Dn&&h("div",{className:"card p-5 mt-4",children:[h("div",{className:"flex justify-between text-xs font-bold",children:[h("span",{children:["QUESTION ",fe+1," / ",T.length," • ",R]}),h("span",{className:"flex gap-1 items-center",children:[a(Kr,{className:"w-3 h-3"})," ",Math.floor(et/60),":",String(et%60).padStart(2,"0")," • Score ",Qt]})]}),a("div",{className:"h-2 bg-[var(--paper)] rounded-full mt-3 overflow-hidden",children:a("div",{className:"h-full bg-[#c9a24b] transition-all",style:{width:`${fe/T.length*100}%`}})}),a("h3",{className:"font-display font-bold text-xl sm:text-2xl leading-tight mt-5",children:T[fe].q}),a("div",{className:"grid sm:grid-cols-2 gap-2 mt-4",children:T[fe].opts.map((f,k)=>{let D="card p-4 text-left font-semibold text-sm";if(bn!==null){if(k===T[fe].ans)D="p-4 text-left font-semibold text-sm rounded-2xl bg-emerald-50 border border-emerald-300";else if(k===bn)D="p-4 text-left font-semibold text-sm rounded-2xl bg-rose-50 border border-rose-300"}return h("button",{onClick:()=>qd(k),className:D,children:[a("span",{className:"font-black text-[#a9842c] mr-2",children:"ABCD"[k]}),f]},k)})}),bn!==null&&h("div",{className:"mt-4 bg-[var(--paper)] rounded-xl p-3 text-sm",children:[a("b",{children:bn===T[fe].ans?"✓ Bonne réponse":"✕ Réponse : "+T[fe].opts[T[fe].ans]})," — ",T[fe].ex]}),a("button",{disabled:bn===null,onClick:jd,className:"btn-gold mt-4 w-full disabled:opacity-40",children:fe+1===T.length?"Voir mon badge":"Question suivante →"})]}),T&&Dn&&Kt&&h("div",{className:"relative overflow-hidden card p-6 mt-4 text-center",children:[a("div",{className:"absolute inset-0 pointer-events-none",children:Array.from({length:22}).map((f,k)=>a("span",{className:"confetti",style:{left:`${k*47%100}%`,background:["#c9a24b","#071631","#e7c87a","#fff"][k%4],animationDelay:`${k%7*0.18}s`}},k))}),a("p",{className:"text-5xl",children:"\uD83C\uDFC5"}),a("p",{className:"text-xs font-black tracking-widest mt-2",children:"BADGE DÉBLOQUÉ"}),h("h3",{className:"font-display font-black text-4xl mt-1",style:{color:"#a9842c"},children:["BADGE ",Kt.n]}),a("p",{className:"font-bold mt-1",children:Kt.msg}),h("p",{className:"text-sm text-[var(--muted)] mt-2",children:["Score : ",Qt," / ",T.length," • Temps : ",Math.floor(et/60)," min ",et%60," s • Progression enregistrée dans cette session."]}),h("div",{className:"flex gap-2 justify-center mt-5",children:[a("button",{onClick:()=>ut(R),className:"btn-gold",children:"Rejouer"}),a("button",{onClick:()=>n("cours"),className:"btn-ghost",children:"Retour aux cours"})]})]})]}),e==="faq"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 06 • FAQ • IA JURIDIQUE"}),a("h2",{className:"font-display font-black text-3xl",children:"Posez votre question de droit"}),h("div",{className:"flex gap-2 bg-amber-50 border border-amber-200 rounded-xl p-3 mt-3 text-xs leading-relaxed",children:[a(br,{className:"w-5 h-5 shrink-0 text-amber-700"}),h("span",{children:[a("b",{children:"IA pédagogique, pas un avocat."})," Cette aide explique et oriente. Pour un cas réel, consultez un professionnel du droit."]})]}),h("div",{className:"card p-4 mt-4 min-h-[300px]",children:[a("div",{className:"space-y-3 max-h-[420px] overflow-auto",children:ga.map((f,k)=>h("div",{children:[a("div",{className:"ml-auto w-fit max-w-[88%] bg-[#071631] text-white rounded-2xl rounded-br-sm px-3 py-2 text-sm",children:f.q}),a("div",{className:"mt-2 bg-[var(--paper)] rounded-2xl rounded-tl-sm px-3 py-3 text-sm whitespace-pre-line leading-relaxed",children:f.a})]},k))}),a("div",{className:"flex flex-wrap gap-1.5 mt-4",children:Q1.map((f)=>a("button",{onClick:()=>Iu(f),className:"chip",children:f},f))}),h("div",{className:"flex gap-2 mt-3",children:[a("input",{value:$u,onChange:(f)=>ka(f.target.value),onKeyDown:(f)=>f.key==="Enter"&&Iu($u),placeholder:"Ex. : Comment contester un licenciement ?",className:"input"}),h("button",{onClick:()=>Iu($u),className:"btn-gold shrink-0 flex items-center gap-1",children:[a(Ht,{className:"w-4 h-4"})," Envoyer"]})]})]})]}),e==="dossiers"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 07 • DOSSIERS DE JUSTICE"}),a("h2",{className:"font-display font-black text-3xl",children:"Soumettre & aider"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"Décrivez un cas, puis recevez des points de vue de la communauté."}),h("div",{className:"grid lg:grid-cols-[380px_1fr] gap-4 mt-4 items-start",children:[h("div",{className:"card p-5",children:[a("h3",{className:"font-display font-bold text-xl",children:"Soumettre un dossier"}),h("div",{className:"space-y-2 mt-3",children:[a("input",{className:"input",placeholder:"Nom complet *",value:ce.nom,onChange:(f)=>It({...ce,nom:f.target.value})}),a("select",{className:"input",value:ce.rang,onChange:(f)=>It({...ce,rang:f.target.value}),children:Mu.map((f)=>a("option",{children:f},f))}),a("select",{className:"input",value:ce.cat,onChange:(f)=>It({...ce,cat:f.target.value}),children:Rd.map((f)=>a("option",{children:f},f))}),a("textarea",{className:"input min-h-[110px]",placeholder:"Décrivez le cas : faits, dates, documents, question précise… *",value:ce.desc,onChange:(f)=>It({...ce,desc:f.target.value})}),a("button",{onClick:rp,className:"btn-gold w-full",children:"Soumettre le dossier"}),wa&&a("p",{className:"text-xs bg-emerald-50 text-emerald-800 rounded-lg p-2",children:wa})]})]}),h("div",{children:[a("div",{className:"flex gap-1.5 overflow-x-auto scrollbar-none pb-2",children:["Tous",...Rd].map((f)=>a("button",{onClick:()=>Qd(f),className:`chip shrink-0 ${Vu===f?"!bg-[#071631] !text-white":""}`,children:f},f))}),a("div",{className:"space-y-3 mt-2",children:At.filter((f)=>Vu==="Tous"||f.cat===Vu).map((f)=>h("article",{className:"card p-4",children:[h("div",{className:"flex flex-wrap gap-2 items-center",children:[a("span",{className:"chip !bg-[#f4e3b0] !text-[#5a4410]",children:f.cat}),a("b",{className:"text-sm",children:f.nom}),h("span",{className:"text-xs text-[var(--muted)]",children:["• ",f.rang]}),h("span",{className:"ml-auto text-xs text-[var(--muted)]",children:[f.aides.length," point(s) de vue"]})]}),a("p",{className:"text-sm leading-relaxed mt-2",children:f.desc}),a("div",{className:"mt-3 space-y-2",children:f.aides.map((k,D)=>h("div",{className:"bg-[var(--paper)] rounded-xl p-3 text-sm",children:[a("b",{children:k.nom})," ",h("span",{className:"text-xs text-[#a9842c] font-bold",children:["• ",k.rang]}),a("p",{className:"mt-1",children:k.txt})]},D))}),h("div",{className:"mt-3 border-t border-dashed pt-3",children:[a("p",{className:"text-xs font-black",children:"AIDER / DONNER SON POINT DE VUE"}),h("div",{className:"grid sm:grid-cols-2 gap-2 mt-2",children:[a("input",{className:"input",placeholder:"Votre nom",value:Ue[f.id]?.nom||"",onChange:(k)=>nl({...Ue,[f.id]:{...Ue[f.id]||{nom:"",rang:"Étudiant",txt:""},nom:k.target.value}})}),a("select",{className:"input",value:Ue[f.id]?.rang||"Étudiant",onChange:(k)=>nl({...Ue,[f.id]:{...Ue[f.id]||{nom:"",rang:"Étudiant",txt:""},rang:k.target.value}}),children:Mu.map((k)=>a("option",{children:k},k))})]}),a("textarea",{className:"input mt-2",placeholder:"Votre analyse, vos étapes, vos précautions…",value:Ue[f.id]?.txt||"",onChange:(k)=>nl({...Ue,[f.id]:{...Ue[f.id]||{nom:"",rang:"Étudiant",txt:""},txt:k.target.value}})}),a("button",{onClick:()=>lp(f.id),className:"btn-navy mt-2 !py-2 text-sm",children:"Publier mon point de vue"})]})]},f.id))})]})]})]}),e==="cercle"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"MODULE 08 • CERCLE"}),a("h2",{className:"font-display font-black text-3xl",children:"Le Cercle des juristes"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"Conversation entre profs, juristes, avocats, juges et étudiants."}),a("div",{className:"flex gap-2 overflow-x-auto scrollbar-none py-3",children:L1.map((f)=>a("button",{onClick:()=>Ad(f),className:`chip shrink-0 ${nt===f?"!bg-[#071631] !text-white":""}`,children:f},f))}),h("div",{className:"card p-4",children:[h("p",{className:"font-bold flex gap-2",children:[a(xr,{className:"w-5 h-5 text-[#a9842c]"})," Salon : ",nt," ",h("span",{className:"text-xs font-normal text-[var(--muted)] ml-auto",children:[(Yt[nt]||[]).length," messages"]})]}),a("div",{className:"space-y-3 mt-4 max-h-[420px] overflow-auto",children:(Yt[nt]||[]).map((f,k)=>h("div",{className:"flex gap-3",children:[a("span",{className:"w-9 h-9 rounded-full bg-[#e7c87a] grid place-items-center text-xs font-black shrink-0",children:f.nom[0]}),h("div",{className:"bg-[var(--paper)] rounded-2xl rounded-tl-sm px-3 py-2.5 flex-1",children:[h("p",{className:"text-xs",children:[a("b",{children:f.nom})," ",h("span",{className:"text-[#a9842c] font-bold",children:["• ",f.rang]})," ",h("span",{className:"text-[var(--muted)]",children:["• ",f.time]})]}),a("p",{className:"text-sm mt-1 leading-relaxed",children:f.txt})]})]},k))}),h("div",{className:"grid sm:grid-cols-[180px_150px_1fr] gap-2 mt-4",children:[a("input",{className:"input",placeholder:"Votre nom",value:Me.nom,onChange:(f)=>tl({...Me,nom:f.target.value})}),a("select",{className:"input",value:Me.rang,onChange:(f)=>tl({...Me,rang:f.target.value}),children:Mu.map((f)=>a("option",{children:f},f))}),h("div",{className:"flex gap-2",children:[a("input",{className:"input",placeholder:"Écrire un message…",value:Me.txt,onChange:(f)=>tl({...Me,txt:f.target.value}),onKeyDown:(f)=>f.key==="Enter"&&Va()}),a("button",{onClick:Va,className:"btn-gold shrink-0",children:a(Ht,{className:"w-4 h-4"})})]})]}),_a&&a("p",{className:"text-xs mt-2 text-emerald-700",children:_a})]}),a("div",{className:"grid sm:grid-cols-3 gap-3 mt-3",children:[["\uD83D\uDCAC","Débats modérés","Respect et sources."],["\uD83C\uDF93","Entraide","Fiches, méthodes, cas pratiques."],["⚖️","Pratique","OHADA, contrats, procédures."]].map(([f,k,D])=>h("div",{className:"card p-4",children:[a("p",{className:"text-2xl",children:f}),a("b",{className:"block mt-2 text-sm",children:k}),a("p",{className:"text-xs text-[var(--muted)]",children:D})]},k))})]}),e==="telechargement"&&h("div",{children:[a("p",{className:"text-xs font-black tracking-widest text-[#a9842c]",children:"TÉLÉCHARGEMENT"}),a("h2",{className:"font-display font-black text-3xl sm:text-4xl",children:"Emportez le Droit partout"}),a("p",{className:"text-sm text-[var(--muted)] mt-1",children:"Cours hors-ligne, quiz, dictionnaire et cercle dans votre poche."}),h("div",{className:"grid md:grid-cols-2 gap-4 mt-5",children:[h("div",{className:"card p-5",children:[a("div",{className:"grid grid-cols-3 gap-2",children:["ANDROID","iOS","WEB"].map((f,k)=>h("button",{onClick:()=>Wu(`Aperçu local — version ${f} : le lien de téléchargement sera activé dans la version publiée.`),className:`rounded-xl p-3 text-center ${k===0?"bg-[#071631] text-white":"bg-[var(--paper)]"}`,children:[a("p",{className:"text-xl",children:["\uD83E\uDD16","\uD83C\uDF4E","\uD83C\uDF10"][k]}),a("b",{className:"text-xs",children:f})]},f))}),h("button",{onClick:()=>Wu("Aperçu local — le téléchargement sera proposé dans la version publiée de l’application."),className:"btn-gold w-full mt-4 flex justify-center gap-2",children:[a(jn,{className:"w-4 h-4"})," Télécharger l’application"]}),h("button",{onClick:up,className:"btn-ghost w-full mt-2 flex justify-center gap-2",children:[a(jr,{className:"w-4 h-4"})," ",Pa?"Lien copié dans le champ !":"Copier le lien de l’appli"]}),Na&&a("p",{className:"text-xs bg-[var(--paper)] rounded-lg p-2 mt-3",children:Na}),Pa&&a("div",{className:"mt-2",children:a("input",{readOnly:!0,value:"Université Droit — Tout le Droit : https://universite-droit.example/app",className:"input text-xs"})}),a("div",{className:"mt-4 space-y-2",children:[["⚡","Accès rapide aux cours"],["\uD83C\uDFC5","Badges et progression"],["\uD83D\uDCAC","Cercle et dossiers"]].map(([f,k])=>h("p",{className:"text-sm",children:[a("span",{className:"mr-2",children:f}),a("b",{children:k})]},k))})]}),h("div",{className:"rounded-3xl p-6 text-white text-center",style:{background:"var(--navy)"},children:[a("p",{className:"text-xs font-black tracking-widest text-[#e7c87a]",children:"SCANNEZ POUR OUVRIR"}),a("div",{className:"w-44 h-44 bg-white rounded-2xl mx-auto mt-4 p-3 grid grid-cols-5 gap-1",children:Array.from({length:25}).map((f,k)=>a("span",{className:"rounded-[2px]",style:{background:k*7%3===0?"#071631":"#e7c87a",opacity:0.9}},k))}),a("p",{className:"font-display font-bold text-xl mt-4",children:"Université Droit"}),a("p",{className:"text-xs text-white/70",children:"QR de démonstration — ne contient pas de lien réel."}),h("div",{className:"flex gap-2 justify-center mt-4",children:[a("span",{className:"chip !bg-white/10 !text-white",children:"★ 4,9"}),a("span",{className:"chip !bg-white/10 !text-white",children:"10 000+ apprenants"})]})]})]})]})]})]}),a("nav",{className:"lg:hidden fixed bottom-0 left-0 right-0 z-40 border-t bg-[var(--surface)]",style:{paddingBottom:"env(safe-area-inset-bottom)"},children:a("div",{className:"flex overflow-x-auto scrollbar-none",children:Qu.map((f)=>{let k=f.icon;return h("button",{onClick:()=>{n(f.id),window.scrollTo({top:0,behavior:"smooth"})},className:"shrink-0 flex flex-col items-center gap-0.5 px-3 py-2 min-w-[68px]",children:[a(k,{className:"w-5 h-5",style:{color:e===f.id?"#a9842c":"var(--muted)"}}),a("span",{className:"text-[10px] font-bold",style:{color:e===f.id?"#a9842c":"var(--muted)"},children:f.label})]},f.id)})})}),h("footer",{className:"max-w-7xl mx-auto px-5 pb-24 lg:pb-8 text-center text-xs text-[var(--muted)]",children:[a("div",{className:"gold-line h-px mb-3"}),a("p",{children:"Université Droit — Tout le Droit • Contenu pédagogique de démonstration. L’IA et les points de vue ne remplacent pas un avocat."})]})]})}Hd.createRoot(document.getElementById("root")).render(a(Wd.default.StrictMode,{children:a(pa,{})}));
</script>
  <script>(function(){function m(a){var h=a.getAttribute("href");if(!h)return;try{var u=new URL(h,document.baseURI);if(((u.protocol==="http:"||u.protocol==="https:")&&u.host!==location.host)||u.protocol==="mailto:"||u.protocol==="tel:"||u.protocol==="sms:"){a.target="_blank";a.rel="noopener noreferrer";}}catch(e){}}function s(){document.querySelectorAll("a[href]").forEach(m);}if(document.readyState!=="loading"){s();}else{document.addEventListener("DOMContentLoaded",s);}document.addEventListener("click",function(e){var a=e.target&&e.target.closest&&e.target.closest("a[href]");if(a){m(a);}},true);})();</script>
  <script type="application/json" data-clippy-inline-media-manifest="1">{"version":1,"slots":[]}</script>
<script>(function(){var loc=location.href.replace(/#.*$/,"");var ATTR_NAMES=["data-product-id","data-productid","data-product_id","product-id","productid","product_id","data-source-entity-id","source-entity-id","source_entity_id","data-product","data-metadata","data-meta"];var DATASET_KEYS=["productId","productid","product_id","sourceEntityId","sourceentityid","source_entity_id","product","metadata","meta"];function readProductId(value){if(typeof value!=="string"||value.length===0)return null;if(/^[0-9]{6,}$/.test(value))return value;var match=value.match(/(?:product(?:_|-)?id|source(?:_|-)?entity(?:_|-)?id)["'=:\s]+([0-9]{6,})/i);return match?match[1]:null}function extractProductId(start){for(var node=start;node&&node!==document.body;node=node.parentElement){for(var i=0;i<ATTR_NAMES.length;i++){var attrValue=node.getAttribute&&node.getAttribute(ATTR_NAMES[i]);var attrProductId=readProductId(attrValue);if(attrProductId)return attrProductId}var dataset=node.dataset||null;if(dataset){for(var j=0;j<DATASET_KEYS.length;j++){var dataValue=dataset[DATASET_KEYS[j]];var dataProductId=readProductId(dataValue);if(dataProductId)return dataProductId}}}return null}function isInlineMediaSlotElement(node){return !!(node&&node.getAttribute&&node.getAttribute("data-clippy-inline-media-slot")!==null)}function findInlineMediaSlot(start){for(var node=start;node&&node!==document.body;node=node.parentElement){if(isInlineMediaSlotElement(node))return node}return null}function readInlineMediaUrl(node){if(!node)return null;return node.getAttribute&&((node.getAttribute("data-clippy-inline-media-url")||node.getAttribute("data-url")||node.getAttribute("data_url")))||node.href||null}function stripHash(url){return String(url).replace(/#.*$/,"")}function urlsMatch(a,b){if(!a||!b)return false;try{return stripHash(new URL(a,loc).href)===stripHash(new URL(b,loc).href)}catch(_){return stripHash(a)===stripHash(b)}}function isFirstPartyReelUrl(value){try{var url=new URL(value,loc);if(url.protocol!=="https:")return false;var host=url.hostname.toLowerCase();var supported=host==="instagram.com"||host.endsWith(".instagram.com")||host==="facebook.com"||host.endsWith(".facebook.com");return supported&&/\/reels?\//i.test(url.pathname)}catch(_){return false}}function isInlineMediaUrlClick(node,href){var slot=findInlineMediaSlot(node);if(!slot)return false;var slotUrl=readInlineMediaUrl(slot);if(slotUrl)return urlsMatch(href,slotUrl);return isFirstPartyReelUrl(href)}function findDataHref(start){for(var node=start;node&&node!==document.body;node=node.parentElement){if(node.getAttribute){var href=node.getAttribute("data-href")||node.getAttribute("data-url");if(href)return{href:href,node:node}}}return null}var nativeOpen=window.open;window.open=function(url){if(parent!==window&&typeof url==="string"&&/^https?:\/\//.test(url)){parent.postMessage({type:"ecto:usercontent-link-click",href:url},"*");return null}return nativeOpen?nativeOpen.apply(window,arguments):null};document.addEventListener("click",function(e){var target=e.target instanceof Element?e.target:null;if(!target)return;if(parent===window)return;var a=target.closest?target.closest("a[href]"):null;if(a&&a.href&&/^https?:\/\//.test(a.href)&&a.href.replace(/#.*$/,"")!==loc){if(isInlineMediaUrlClick(a,a.href))return;var productId=extractProductId(target)||extractProductId(a);if(productId){e.preventDefault();parent.postMessage({type:"ecto-artifact-link-click",productId:productId},"*");return}e.preventDefault();parent.postMessage({type:"ecto:usercontent-link-click",href:a.href},"*");return}var dataHref=findDataHref(target);if(dataHref&&/^https?:\/\//.test(dataHref.href)&&dataHref.href.replace(/#.*$/,"")!==loc){if(isInlineMediaUrlClick(dataHref.node,dataHref.href))return;e.preventDefault();parent.postMessage({type:"ecto:usercontent-link-click",href:dataHref.href},"*")}},true)})();</script><script>(function(){var FOCUS_TYPE="ecto:artifact-focus-request";var CLOSE_TYPE="ecto:artifact-close-request";function focusArtifactDocument(){var body=document.body;if(!body)return;try{window.focus();}catch(e){}if(!body.hasAttribute("tabindex"))body.setAttribute("tabindex","-1");try{body.focus({preventScroll:true});}catch(e){try{body.focus();}catch(e2){}}}window.addEventListener("message",function(event){if(event.source!==window.parent)return;var data=event.data;if(!data||typeof data!=="object"||data.type!==FOCUS_TYPE)return;if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",focusArtifactDocument,{once:true});return;}focusArtifactDocument();});window.addEventListener("keydown",function(event){if(event.key!=="Escape")return;window.setTimeout(function(){if(event.defaultPrevented)return;window.parent.postMessage({type:CLOSE_TYPE},"*");},0);});})();</script></body>
</html>
'''


@app.route("/")
def index():
    return Response(HTML_PAGE, mimetype="text/html")


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
