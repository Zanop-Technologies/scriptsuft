# Scriptsuft

The official language for developing apps in all Zanop OS types, this is markup based and uses XML.

## Sample

This is a simple app when you create one (Scriptsuft is based off WML)

```xml
<!DOCTYPE wml PUBLIC "-ZTECH//DTD/WML.dtd" "WML.dtd">
<wml version="1.0" lang="en">
  <PackageIdentifier>
     <PackageDestination=
        -folder="/main/apps/pkg.example.com" />
     <PackageTitle=
        -title="Example" />
     <PackageAuthor=
        -author="John Doe" />
  </PackageIdentifier>
  <head>
     <meta charset="UTF-8" />
     <content type="autosize" />
  </head>
  <body>
    <h1>My First App!</h1>
    <p>This is my first app with ScriptSuft!</p>
  </body>
</wml>
```

## Learn The Language

Check `docs/` to learn ScriptSuft.