# Code Style

## Terminology
The key words SHOULD, MUST, SHOULD NOT, MUST NOT and MAY are used throughout this document in accordance to RFC 2119 to describe the significance of the specification's requirements.

## Styleguide
All newly written code should follow StandardJS 16.0.3 (or the equivalent ts-standard) if applicable.

## Regarding TypeScript
TypeScript MUST follow the same rules as regular JavaScript. See ts-standard.

## Comments
All code SHOULD be fairly commented in a manner that enhances the understanding and readability of the code using standard javascript comments.

```javascript
/*
  Multiline
*/

// Singleline
```

## JSDoc
JSDoc MUST be used to document functions, variables and other aspects of the code to easily understand what it does and to simplify interaction with it through for example autocompletion. Note however that JSDoc is a technical documentation complementing regular documentation and is not its replacement.

```javascript
/**
 * Sums two numbers
 * @param { Number } a
 * @param { Number } b
 * @returns { Number }
 */
function sum (a, b) {
  return a + b
}
```

## Constants
True constants MUST be named in uppercase with underscores replacing spaces in order to clearly state that it is truly immutable, thay are usually placed close to or at the start of a file. A constant should be documented and may even include the unit in its name (see example below.)

### The const keyword
Javascript provides the keyword const for denoting a read-only variable, however, using this keyword will still allow writing to a reference type variable. That is objects and its subtypes such as arrays. Therefore using the const keyword doesn't equal a true constant.

## Stylesheets
All newly written stylesheets SHOULD follow the SUIT naming convention. This however only applies to the naming convention of CSS stylesheets and not any other languages or helper libraries, which are optional.
