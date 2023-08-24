function random_color(id){	
    color = 'hsla('+ 360 * Math.random() +', 70%,  72%, 0.8)';	
    document.getElementById(id).style.backgroundColor = color	
    document.getElementById(id).style.boxShadow = "0 0 20px 10px " + color	
}	