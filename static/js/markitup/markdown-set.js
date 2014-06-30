// ----------------------------------------------------------------------------
// markItUp!
// ----------------------------------------------------------------------------
// Copyright (C) 2008 Jay Salvat
// http://markitup.jaysalvat.com/
// ----------------------------------------------------------------------------
myMarkdownSettings = {
    nameSpace:          'markdown', // Useful to prevent multi-instances CSS conflict
    onShiftEnter:       {keepDefault:false, openWith:'\n\n'},
    markupSet: [
        {name:'h1', key:"1", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '=') } },
        {name:'h2', key:"2", placeHolder:'Your title here...', closeWith:function(markItUp) { return miu.markdownTitle(markItUp, '-') } },
        {name:'h3', key:"3", openWith:'### ', placeHolder:'Your title here...' },
        {name:'h4', key:"4", openWith:'#### ', placeHolder:'Your title here...' },
        {name:'h5', key:"5", openWith:'##### ', placeHolder:'Your title here...' },
        {name:'h6', key:"6", openWith:'###### ', placeHolder:'Your title here...' },
        {name:'<b>b</b>', key:"B", openWith:'**', closeWith:'**'},
        {name:'<i>i</i>', key:"I", openWith:'_', closeWith:'_'},
        {name:'ol', openWith:function(markItUp) {
            return markItUp.line+'. ';
        }},
        {name:'img', key:"P", replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},
        {name:'url', key:"L", openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
        {name:'quotes', openWith:'> '},
        {name:'code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
    ]
}

// mIu nameSpace to avoid conflict.
miu = {
    markdownTitle: function(markItUp, char) {
        heading = '';
        n = $.trim(markItUp.selection||markItUp.placeHolder).length;
        for(i = 0; i < n; i++) {
            heading += char;
        }
        return '\n'+heading+'\n';
    }
}
