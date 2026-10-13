# Code Style

## Terminology
The key words MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, AVOID and ALWAYS are used throughout this document following RFC 2119 to describe the significance of the specification's requirements. AVOID and ALWAYS are local additions beyond RFC 2119.

## Encoding
Use UTF-8 if possible.

## Design Principles
You MUST use our software design principles to our code as laid out in software-design-principles.md

## JavaScript
### Styleguide
All newly written code SHOULD follow the latest StandardJS release if applicable. Source: https://standardjs.com/

### Regarding TypeScript
TypeScript MUST follow the same rules as regular JavaScript. See ts-standard.

### Comments
All code SHOULD be commented in a manner that enhances the understanding and readability of the code using standard JavaScript comments.

```javascript
/*
  Multiline
*/

// Single line
```

### JSDoc
JSDoc MUST be used to document functions, variables and other aspects of the code to easily understand what it does and to simplify interaction with it through for example autocompletion. Note however that JSDoc is a technical documentation complementing regular documentation and is not its replacement.

```javascript
/**
 * Sums two numbers
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 */
function sum (a, b) {
  return a + b
}
```

In TypeScript, types MUST be declared in the signature; JSDoc carries the description:

```typescript
/**
 * Sums two numbers
 * @param a - The first number
 * @param b - The second number
 * @returns The sum of a and b
 */
function sum (a: number, b: number): number {
  return a + b
}
```

### Constants
True constants MUST be named in uppercase with underscores replacing spaces in order to clearly state that it is truly immutable, they are usually placed close to or at the start of a file. A constant SHOULD be documented and may even include the unit in its name.

```javascript
/** Maximum number of retry attempts before giving up */
const MAX_RETRY_COUNT = 3

/** Delay between polling attempts, in milliseconds */
const POLL_INTERVAL_MS = 500
```

#### The const keyword
JavaScript provides the keyword const for denoting a read-only variable, however, using this keyword will still allow writing to a reference type variable. That is objects and its subtypes such as arrays. Therefore using the const keyword doesn't equal a true constant.

## CSS
### Stylesheets
All newly written stylesheets SHOULD follow the OOCSS naming convention. This however only applies to the naming convention of CSS stylesheets and not any other languages or helper libraries, which are optional. OOCSS (Object-Oriented CSS) is a CSS methodology that promotes modularity, reusability, and separation of concerns. It advocates treating CSS classes as objects, encapsulating their styles and properties, and using them to compose user interfaces. OOCSS operates on two main rules: 1) Separation of structure and skin and 2) Separation of container and content. 
```html
<nav class="nav"> 
    <ul class="list nav-list"> 
        <li class="list-item nav-item"> 
            <a href="/about" class="link nav-link">About</a> 
        </li> 
        <li class="list-item nav-item"> 
            <a href="/pricing" class="link nav-link">Pricing</a> 
        </li> 
        <li class="list-item nav-item"> 
            <a href="/contact" class="link nav-link">Contact</a> 
        </li> 
    </ul> 
</nav>
```
### Libraries
AVOID libraries like SCSS, SASS, Tailwind or Bootstrap where normal vanilla CSS can achieve the same job.

### Always reset first
Reset stylesheets first to write efficient code.
```css
*,
*::after,
*::before {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:where(html) {
  color-scheme: light dark;
  hanging-punctuation: first allow-end last;
  interpolate-size: allow-keywords;
  scroll-behavior: smooth;
  scrollbar-gutter: stable;
  text-size-adjust: none;
  -webkit-text-size-adjust: none;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-smoothing: antialiased;
}

:where(html.translated-rtl) {
  direction: rtl;
}

@media (prefers-reduced-motion: reduce) {
  :where(html) {
    scroll-behavior: auto;
  }
}

:where(body) {
  min-block-size: 100svb;
  min-inline-size: 300px;
}

:where(canvas, img, picture, svg, video) {
  block-size: auto;
  border: none;
  display: block;
  max-inline-size: 100%;
}

:where(button, input, progress, select, textarea) {
  appearance: none;
  background: transparent;
  border: none;
  color: inherit;
  font: inherit;
  hanging-punctuation: none;
  line-height: inherit;
  text-align: start;
  touch-action: manipulation;
}

:where(button) {
  cursor: pointer;
  user-select: none;
}

:where(textarea) {
  resize: vertical;
}

:where(textarea:not([rows])) {
  field-sizing: content;
}

:where(fieldset, iframe) {
  border: none;
}

:where(p, li, h1, h2, h3, h4, h5, h6) {
  overflow-wrap: break-word;
  text-wrap: pretty;
}

:where(abbr[title]) {
  border: none;
  text-decoration: none;
}

:where(cite) {
  font-style: inherit;
}

:where(small) {
  font-size: inherit;
}

:where(li, ol, ul) {
  list-style: none;
}

:where(dialog, [popover]) {
  background: transparent;
  border: none;
  color: inherit;
  margin: auto;
  max-block-size: none;
  max-inline-size: none;
  position: fixed;
}

:where([popover]) {
  inset: auto;
}

:where(dialog:not([open], [popover]), [popover]:not(:popover-open)) {
  display: none;
}

:where([hidden]:not([hidden="until-found"])) {
  display: none !important;
}

```
### Units
Declarations SHOULD be dynamic/responsive first. AVOID fixed values in pixels, centimeters, millimeters unless absolutely necessary. 
### Structure
CSS SHOULD be structured "outside->in", starting with html, body, and then the structural elements of the page/view. It SHOULD follow the cascading properties and AVOID repetition according to KISS. If it can be reused, then set the CSS as far out as possible. 
Example:
```css
/*Import reset*/
/*Import fonts*/
/*Define animations*/
/*Define CSS-variables and/or properties*/
:root {
  --primary-bg-color: green; /* global scope */
}
@property --my-color {
  syntax: "<color>";
  inherits: true;
  initial-value: lightgray;
}
/*Define CSS-rules, ordered outside->in*/
html {
  background-color: var(--primary-bg-color);
}
body {}
header {}
nav {}
main {}
footer {}
#unique-id {}
.not-unique-class {}
```
### Naming conventions
MUST be semantic. Always lower-case for class and id names. AVOID using classes where semantic naming is sufficient. Example: If an H2 is used semantically, you don't need to use `h2.subtitle` to define it and instead refer to it as `.article h2`.
Example:
```css
#main-nav {}
.nav-link {}
```
## HTML
ALWAYS write semantic code according to HTML5. Use a 4-space indent rather than tabs.
### Skeleton and structure
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page Title</title>
    <link rel="stylesheet" href="">
</head>
<body>

    <img src="img_la.jpg" alt="Los Angeles" id="best-image">

    <main>
        <h1>This is a Heading</h1>
        <p>This is a paragraph.</p>
        <p>This is another paragraph.</p>
        <div class="not-unique-identifier"></div>
    </main>
    <aside>
        <div id="unique-identifier"></div>
        <div class="not-unique-identifier"></div>
    </aside>

    <script src=""></script>

</body>
</html>
```
### Usability
ALWAYS think of the user and intended target group when applying usability. Aim for WCAG compliance.
### Minimizing and Normalizing
When reading code, ALWAYS normalize it if it is minimized rather than reading it in one big chunk.
When making production-ready code for delivery, it SHOULD be minimized. Make this part of the build step.

