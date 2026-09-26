# Linking Multiple Files

You can link multiple files using two methods, the first one being adding a `linker.yaml` into your `main.srp` or use the `class file` method which is used to manually link files.

## Methods

### Linker

To use the linker method, create a file named `linker.yaml` in the root folder of your project, assuming you have created it, the file should contain this:

```yaml
files:
  getFile: "/path/to/your/other/file",
  limitFile: 5, # Can be any integer
  extensionDetect: "*.srt" # Optional 
```

### Class File

To use the `class file` method, you will have to use `!indef json` and the `jsonblock{}` function, you will also have to use the explicit directories of the file you want to link.

```text
!indef system
!indef json
!indef func(print)
!indef is console

jsonblock{
    {
        "file1": "/path/to/your/file"
    }
}

speak if jsonblock(=)("Your files are loaded")
# Note: You can add as many files as you want
```