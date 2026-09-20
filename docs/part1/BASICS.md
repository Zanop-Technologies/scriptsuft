# Basics

In this guide, you will be learning the **Basics** of Scriptsuft. You will learn the syntax of Scriptsuft such as:

- `<!DOCTYPE>`
- `<wml>`
- `<PackageIdentifer>`
- `<PackageDestination>`
- `<PackageAuthor>`

and many more.

## Explanation of Syntax

### Main Syntax


`<!DOCTYPE>` — Tells Zanop OS What this file is.

`<wml>` — Body of the Scriptsuft (Website Markup Language) app.

`<head>` — Contains the elements that identify the documents charset, title and many more.

`<body>` — Body of the app.

### Text 

`<h1> to <h6>` — Header level, Header 1 is the largest level while Header 6 is the smallest level.

`<p>` — Paragraph.

`<mp>` — Multiple Paragraphs

`<text>` — Similar to HTMLs `<span>` element.

`<code>` — Shows monospace text.

### Seperators

`<breakline>` — Puts an empty space.

`<line>` — Puts a line seperator.

### Package Identifiers

`<PackageIdentifer>` — Body of the Package Identifer.

`<PackageAuthor>` — Author of the package.

`<PackageTitle>` — Title of the Package.

`<PackageDestination>` — Where the package will be installed.

### Styling

`<theme>` — Targets a specific element to turn into a specific color.

---


## Making a Simple App
To make a simple app in Scriptsuft, you need these tools:

- VSCode or any IDE
- NodeJS v20.19.2 and up.
- Web Browser (since Scriptsuft is based off WML and can run in a browser)
- Virtual Machine (optional if you want to run it in Zanop OS, however for beginners, Zanop OS recommends to do it in a browser.)

1. Open VSCode or any IDE (This tutorial uses AntiX Linux, your Operating System depends. The IDE we will be using is Codium.)

![Illustration 1](/assets/illustrations/illustration1.jpg)

> *Note: You can choose between the start menu or the desktop.*

2. Open a folder, name it anything you want.

![Illustration 2](/assets/illustrations/illustration2.jpg)

3. After creating your folder, create these folders and files that are needed for your first app.

```text
your-project-name/
├── .identifer/       
│   ├── identify.toml
│   └── info.toml
├── .instructions/
│   ├── compile.js 
│   └── compile-instructions.yaml
└── home.wml
```

4. What should these files contain?

Your `identify.toml` and `info.toml` should contain the following:

`identify.toml`
---

```toml
[info-file]
info-file = "/.identifer/info.toml"

[config]
# Optional, it will create it automatically 
# within .identifier/
config-src = "/.identifier/settings.toml"
```

`info.toml`
---

```toml
[author]
author = "Your Name/Username Here"

[title]
title = "your-package-name"

[description]
description = "The description of your package."

[type]
# Default is GUI
# or you can set it to
# text.
type = "GUI"
```

Then, your compile.js and compile-instructions.toml should contain:

`compile.js`
---

```javascript
// Code will be made
```