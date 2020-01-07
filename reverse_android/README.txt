### apktool工具
官方文档为：https://ibotpeaches.github.io/Apktool/documentation/
它主要时用来解包和打包

### re-sign.jar
重签名工具，可以快速签名

### bytecode-view
多种模式查看.class文件,包括逆向出java,直接查看字节码

### jd-gui
查看.class文件，jar包，其实是逆向出了.class文件变成java文件

### dex2jar工具包
把各种dex转化为jar包

### smali2java工具
目前采用apktool解出来的包基本都是smali文件，采用此工具打开smali文件可以转化为java代码阅读
但是此工具有局限性，说明如下：
`smali2java工具基于apktool v1.5.0（baksmali v1.3.4）生成的smali文件，依赖于smali文件中的代码行数（.line关键字）和变量别名（.local关键字）等信息，可以最大程度还原原始的java代码。还原出的java代码将具有原始的变量命名，代码的顺序也与原始的java代码保持一致。因此，本工具也具有局限性，仅适用于带有行数和变量别名信息的smali文件（java编译器的编译选项可以在生成的字节码中剔除这些信息）`

### baksmali工具
把dex逆向成smali文件