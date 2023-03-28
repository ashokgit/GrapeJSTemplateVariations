from analyzer.HTMLDecoder import HTMLDecoder
from analyzer.HTMLEncoder import HTMLEncoder
from analyzer.HTMLAnalyzer import HTMLAnalyzer
import json 
import re

html_content = '''<body><style>
      
    body { background-color: #fff }
    * ::-webkit-scrollbar-track { background: rgba(0, 0, 0, 0.1) }
    * ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2) }
    * ::-webkit-scrollbar { width: 10px }
  

      [data-gjs-type="wrapper"] {
        min-height: 100vh;
        padding-top: 0.001em;
      }

      .gjs-dashed *[data-gjs-highlightable] {
        outline: 1px dashed rgba(170,170,170,0.7);
        outline-offset: -2px;
      }

      .gjs-selected {
        outline: 2px solid #3b97e3 !important;
        outline-offset: -2px;
      }

      .gjs-selected-parent {
        outline: 2px solid #ffca6f !important
      }

      .gjs-no-select {
        user-select: none;
        -webkit-user-select:none;
        -moz-user-select: none;
      }

      .gjs-freezed {
        opacity: 0.5;
        pointer-events: none;
      }

      .gjs-no-pointer {
        pointer-events: none;
      }

      .gjs-plh-image {
        background: #f5f5f5;
        border: none;
        height: 100px;
        width: 100px;
        display: block;
        outline: 3px solid #ffca6f;
        cursor: pointer;
        outline-offset: -2px
      }

      .gjs-grabbing {
        cursor: grabbing;
        cursor: -webkit-grabbing;
      }

      .gjs-is__grabbing {
        overflow-x: hidden;
      }

      .gjs-is__grabbing,
      .gjs-is__grabbing * {
        cursor: grabbing !important;
      }

      
        [data-gjs-type="wrapper"] {
          padding: 10px;
        }
        
      * { box-sizing: border-box; } body {margin: 0;}
    </style><section id="ik7m" data-gjs-type="default" draggable="true" data-version="1.2" class="section section-column-1 sectionHeader-left"><div id="isdj" data-gjs-type="default" class="header-wrapper automatic-spacing"><div id="iv6m" data-gjs-type="default" class="menu-col-0"><span id="i75o" data-gjs-type="text" class="section-heading font-header color-primary">DESSERTS</span><span id="ikgv" data-gjs-type="text" class="section-header-price font-body">10$</span></div></div><div id="i8gt9" data-gjs-type="default" draggable="true" as="menu-item" data-version="2.1" class="menu-item menu-item-3 automatic-spacing"><table id="i84ay" data-gjs-type="table"><tbody id="ib6hs" data-gjs-type="tbody"><tr id="ij2p8" data-gjs-type="row"><td id="iidj6" data-gjs-type="cell"><div id="imaf3" data-gjs-type="text" class="menu-item-title font-title">Key Lime Pie</div></td></tr><tr id="idwon" data-gjs-type="row"><td id="ikmjb" data-gjs-type="cell"><div id="i2zq1" data-gjs-type="text" class="menu-item-description font-body">Graham cracker crust, key lime filling topped with whipped cream</div><div id="ibhar" data-gjs-type="text" class="menu-item-price font-body">$12</div></td></tr><tr id="i0k6i" data-gjs-type="row"><td id="iblf6" data-gjs-type="cell"><div id="i6x6n" data-gjs-type="text" class="menu-item-add-on font-body">Add on</div></td></tr></tbody></table></div><div id="i0slc" data-gjs-type="default" draggable="true" as="menu-item" data-version="2.1" class="menu-item menu-item-3 automatic-spacing"><table id="imzfv" data-gjs-type="table"><tbody id="is9y5" data-gjs-type="tbody"><tr id="iolvg" data-gjs-type="row"><td id="it2k9" data-gjs-type="cell"><div id="imnvc" data-gjs-type="text" class="menu-item-title font-title">Apple Pie a La Mode</div></td></tr><tr id="itufn" data-gjs-type="row"><td id="imtvj" data-gjs-type="cell"><div id="iwuhl" data-gjs-type="text" class="menu-item-description font-body">Fresh baked apple pie topped with vanilla ice cream</div><div id="iubvf" data-gjs-type="text" class="menu-item-price font-body">$13</div></td></tr><tr id="ifcb2" data-gjs-type="row"><td id="imon7" data-gjs-type="cell"><div id="i8emm" data-gjs-type="text" class="menu-item-add-on font-body">Add on</div></td></tr></tbody></table></div><div id="i80ts" data-gjs-type="text" class="align-center section-footer-price">10$</div><div id="i6yob" data-gjs-type="text" class="align-center section-add-on">Add on</div><section data-gjs-highlightable="true" id="iy1av" data-gjs-type="default" draggable="true"></section></section><div data-gjs-highlightable="true" id="icy8" data-gjs-type="wrapper" class=""><footer data-gjs-highlightable="true" id="im1gx" data-gjs-type="default" draggable="true" class="footer background-primary color-background flapjackFooter" data-version="1.8"><div data-gjs-highlightable="false" id="i4mqg" data-gjs-type="text" draggable="true" class="footer-text">123 Menu St. 1(800) FLP-JACK<br>Made with ♥ by Flapjack.co</div></footer></div><div class="gjs-css-rules"><div id="gjs-css-rules"><style>div img{max-width:100%;}</style><style>.flapjackFooter span{color:red;}</style><style>.align-left{text-align:left;}</style><style>.align-center{text-align:center;}</style><style>.align-right{text-align:right;}</style><style>.divider{background-color:#029F9A;height:2px;}</style><style>.header{display:flex;align-items:center;width:calc(100% + 24px);margin-left:-12px;margin-top:-12px;margin-bottom:12px;}</style><style>.header img{display:table-cell;height:120px;}</style><style>.header-image-center img{margin:auto;}</style><style>.header-image-right img{margin-left:auto;}</style><style>.footer{width:100%;text-align:center;position:fixed;bottom:0;padding:8px 8px 12px;right:0;}</style><style>.section{display:flex;flex-direction:column;justify-content:space-between;padding:12px;z-index:1;position:relative;}</style><style>spacer{display:inline-block;}</style><style>.menu-item{width:100%;border-spacing:0;}</style><style>.menu-item tbody{z-index:5;position:relative;}</style><style>#icy8{font-size:20px;}</style><style>body{color:#029F9A;background-color:#ffffff;}</style><style>@font-face{font-family:DexaPro-400-Regular;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673479343679-DexaPro-400-Regular");}</style><style>@font-face{font-family:DexaPro-900-Black-Italic;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673480841869-DexaPro-900-Black-Italic");}</style><style>@font-face{font-family:DexaPro-900-Black-Italic;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673480841011-DexaPro-900-Black-Italic");}</style><style>.font-title{font-family:DexaPro-900-Black-Italic;font-size:28px;}</style><style>.font-header{font-family:DexaPro-900-Black-Italic;font-size:49px;}</style><style>.font-body{font-size:20px;}</style><style>.background-primary{background-color:#029F9A;}</style><style>.background-secondary{background-color:#029F9A;}</style><style>.background-tertiary{background-color:#029F9A;}</style><style>.color-primary{color:#029F9A;}</style><style>.color-secondary{color:#029F9A;}</style><style>.color-tertiary{color:#029F9A;}</style><style>.color-background{color:#ffffff;}</style><style>@font-face{font-family:DexaPro-400-Regular;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673479343679-DexaPro-400-Regular");}</style><style>@font-face{font-family:DexaPro-900-Black-Italic;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673480841869-DexaPro-900-Black-Italic");}</style><style>@font-face{font-family:DexaPro-900-Black-Italic;src:url("https://oobtxuazqbzntvhmvjtj.supabase.co/storage/v1/object/public/fonts/766688b9-5533-4fcb-8807-b02c7b76b6af-1673480841011-DexaPro-900-Black-Italic");}</style><style>[data-gjs-type="wrapper"]{padding-top:12px;padding-bottom:0;padding-left:12px;padding-right:12px;}</style><style>.footer-2{position:fixed;width:100%;bottom:0;right:0;padding:0px 33px 20px 33px;}</style><style>.footer-2 .footer-content{padding-top:15px;display:flex;align-items:center;justify-content:space-between;}</style><style>.footer-2 .footer-content.footer-content-solid{border-top:2px solid #029F9A;}</style><style>.footer-2 .footer-content.footer-content-dashed{border-top:2px dashed #029F9A;}</style><style>.color-menu{color:#d91c1c;}</style><style>#isdj{display:flex;text-align:left;}</style><style>#iv6m{width:100%;}</style><style>#ikgv{display:none;margin-left:5px;}</style><style>#i8gt9{padding:0px;}</style><style>#i2zq1{display:inline;}</style><style>#ibhar{display:inline;margin-left:10px;}</style><style>#i6x6n{display:none;}</style><style>#i0slc{padding:0px;}</style><style>#iwuhl{display:inline;}</style><style>#iubvf{display:inline;margin-left:10px;}</style><style>#i8emm{display:none;}</style><style>#i80ts{display:none;}</style><style>#i6yob{display:none;}</style><style>.automatic-spacing{margin-bottom:43px;}</style></div><div id="gjs-css-rules-576"></div><div id="gjs-css-rules-420"></div></div><div class="gjs-js-cont"></div><iframe id="_hjSafeContext_29028236" title="_hjSafeContext" tabindex="-1" aria-hidden="true" src="about:blank" style="display: none !important; width: 1px !important; height: 1px !important; opacity: 0 !important; pointer-events: none !important;"></iframe></body>'''  # Your HTML content here


encoder = HTMLEncoder()
decoder = HTMLDecoder()

json_output = encoder.encode(html_content)
html_output = decoder.decode(json_output)

# print("JSON Output:")
# print(json_output)

# print("HTML Output:")
# print(html_output)

analyzer = HTMLAnalyzer(json_output)
print('---- BEFORE -----------')
print(analyzer.css_rules)

analysis_result = analyzer.analyze()

# We will use the above analysis_result to pass it to gpt in the below prompt
# // System: You are a UI/UX Expert. You have a deep understanding of advanced color theory, fonts and spacing.
# Original Design Preference:
# {analysis_result}
# Pick all important elements and make a variation scheme for a 'Traditional Chinese Resturant' in the given format below
# suggested_changes = [
#     {
#         'selector': '',
#         'property': ',
#         'new_value': ''
#     },
#    {
#         'selector': '',
#         'property': ',
#         'new_value': ''
#     },
# ]
# Suggested Design Preference: 
# suggested_changes = [
#     {

# Stop word: ]

# CALL GPT-3.5 completion api here

suggested_changes = [
    {
        'selector': 'body',
        'property': 'background-color',
        'new_value': '#FFCE64'
    },
    {
        'selector': 'body',
        'property': 'color',
        'new_value': '#000'
    },
    {
        'selector': '.background-primary',
        'property': 'background-color',
        'new_value': '#FFCE64'
    },
    {
        'selector': '.background-secondary',
        'property': 'background-color',
        'new_value': '#FFCE64'
    },
    {
        'selector': '.background-tertiary',
        'property': 'background-color',
        'new_value': '#FFCE64'
    },
    {
        'selector': '.color-primary',
        'property': 'color',
        'new_value': '#000'
    },
    {
        'selector': '.color-secondary',
        'property': 'color',
        'new_value': '#000'
    },
    {
        'selector': '.color-tertiary',
        'property': 'color',
        'new_value': '#000'
    },
    {
        'selector': '.color-background',
        'property': 'color',
        'new_value': '#FFCE64'
    },
    {
        'selector': '.color-menu',
        'property': 'color',
        'new_value': '#000'
    },
    {
        'selector': '#iubvf',
        'property': 'margin-left',
        'new_value': '0'
    }
]

# print("Analysis Result:")
# print(analysis_result)

analyzer.apply_changes(suggested_changes)
print('---- AFTER -----------')
print(analyzer.css_rules)


# Replace the new css rules in the html template again
# replace the original template

with open('./data/json_output.txt', 'w') as file:
        output = re.sub(' +', ' ', json.dumps(json_output['html_structure']))
        file.write(output)