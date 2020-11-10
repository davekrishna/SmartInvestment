function undoFunct()
    {
        document.execCommand('undo',false,'')
    }
function redoFunct()
    {
        document.execCommand('redo',false,'')
    }
function alignRight()
    {
        document.execCommand('justifyRight',false,'')
    }
function alignLeft()
    {
        document.execCommand('justifyLeft',false,'')
    }
function alignCenter()
    {
        document.execCommand('justifyCenter',false,'')
    }
function justifyContent()
    {
        document.execCommand('justifyFull',false,'')
    }
function makeBold()
    {
        document.execCommand('bold', false, '');
    }
function makeItalic()
    {
        document.execCommand('italic', false, '');
    }
function Underline()
    {
        document.execCommand('underline', false, '');
    }
function LinkSelection()
    {
        var url = prompt("Enter the URL");
        console.log(url)
        document.execCommand("createLink", false, url);
    }
function unLinkSelection()
{
    document.execCommand('unlink',false,'')
}
function createSubscript()
{
    document.execCommand('subscript',false,'');
}
function createSuperscript()
{
    document.execCommand('superscript',false,'')
}
function Cut()
{
    document.execCommand('cut',false,'')
}
function addParagraph()
{
    document.execCommand('insertParagraph',false,'')
}
function addImage()
{
    var url = prompt("Enter the URL");
    console.log(url)
    document.execCommand("insertImage",false, url);
}
function highlightContent()
{
    var colorCode = prompt("Enter the hex value of the color to be used to highlight");
    document.execCommand('styleWithCSS',true)
    document.execCommand("HiliteColor", true,colorCode)
    document.execCommand('styleWithCSS',false)
}
function deleteContent()
{
    document.execCommand('delete',false,'')
}
