# Development Preferences

## Package Manager
Use npm as preferred package manager. If the current project uses a different package manager, use that instead if possible.

## JavaScript
Use vanilla Javascript where possible for templates and single webpages.

## Node.js
Use the same Node.js version across projects or environments.

## Ports
To avoid conflicts with other self-developed apps, use ports in the 6000 range. Avoid any conflicts with existing apps or known conflicts.

## Server
Always check if the server is already running before suggesting to start it.

## Portable Apps
When building apps for Windows, Mac and Linux make sure the apps are portable, or can be run without installation unless specifically directed to create an installer.

Windows users are usually locked down due to security and cannot install software on their own, but can run software.

Make sure users are not blocked by Windows or MacOS security.

Avoid dependencies to adjecent folders and make the apps as self-contained as possible.

## Prettify minified code
When encountering minified code that is hard to read, run a prettify script to make the code readable and structured.

## Base64 encoded content
When encountering base64 encoded content that are images, videos or other binary content, mark them with comments in beginning and end, and then skip that data when reading code.
