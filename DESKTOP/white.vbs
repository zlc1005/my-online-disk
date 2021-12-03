set xda=createobject("wscript.shell")
While True
msgbox("aaa")
Dim Word
Set Word = CreateObject("Word.Application")
Word.Documents.Add
Word.Selection.PasteAndFormat(wdFormatPlainText)
Word.Selection.WholeStory
str = Word.Selection.Text
Word.Quit(False)
wscript.sleep(2000)
xda.sendKeys(str)
wscript.sleep(3000)
Wend
wscript.quit()