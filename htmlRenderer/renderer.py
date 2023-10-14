

def div(_class="", content=""):
    text = []
    if _class != "":
        text.append(f"<div class={_class}>")
    else:
        text.append(f"<div>")
    
    text.append("  " + content)

    text.append("</div>")
    return text



page = []
page.append(div("conatainer","<p>Hello World</p>"))

for component in page:
    for line in component:
        print(line)

#the issue with this is that we can't nest components.
#as we wont be able to append the text if the content in the div is itself is a list
