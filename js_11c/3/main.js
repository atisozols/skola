// realizēt dark mode pogas funkcionalitāti

function switch_theme(){
    link = document.head.getElementsByTagName("link")[0]
    link.href = "dark.css"
}

// Pamatā balta lapa ar tumšu tekstu -> Pamatā tumšu lapu ar gaišu tekstu