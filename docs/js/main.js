
var regions = []
regions['Puglia'] = "http://www.ingegnosohidalgo.it/img/mappa_regioni/puglia.jpg";

$('.region').hover(function(){
    var current_region = $(this).attr('id')
    $('#mappa_regioni').attr("src",regions[current_region]);
})

$('#mappa_regioni').mouseout(function(){
    $('#mappa_regioni').attr("src","img/mappa_regioni.jpg");
})


$('.region').click(function(){
    var current_region = $(this).attr('id')
    
    $('#current_region').load("html/Puglia.html");
})
