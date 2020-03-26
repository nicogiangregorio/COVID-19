function adjustPlot() {
  window_height = $(window).height() * 0.8;
  
  if($('#graph1').length && $('#graph2')) {
    var width_graph1 = $('#graph1').innerWidth();
    var pad_left_graph1  = parseInt($('#graph1').css('margin-left'));
    var pad_right_graph1 = parseInt($('#graph1').css('margin-right'))
    
    var max_width_graph1 = width_graph1 + pad_left_graph1 + pad_right_graph1
    var graph1_id = $('#graph1 > div > div > div').attr('id')
    var graph2_id = $('#graph2 > div > div > div').attr('id')
    
    Plotly.relayout(graph1_id, {width: max_width_graph1, height: window_height})
    Plotly.relayout(graph2_id, {width: max_width_graph1, height: window_height})
    
    $('#graph2').css('margin-top', '75px')
  }
}

window.addEventListener('resize', adjustPlot);
window.addEventListener('load', adjustPlot);

$("#italy_map").vectorMap({
    map: 'it_regions_mill', 
    zoomOnScroll: false,
    zoomButtons : false,
    backgroundColor: "white", 
    panOnDrag: false,
    regionStyle: {
        initial: {
          fill: '#2E3561',
          "fill-opacity": 1,
          stroke: 'none',
          "stroke-width": 0,
          "stroke-opacity": 1
        },
        hover: {
            fill: '#9CC2C5',
            cursor: 'pointer'
        },
        selected: {
          fill: '#9CC2C5'
        }
      },
      onRegionClick: function(e, code) {
        $('#current_region').load("html/" + code + ".html", function(){
          adjustPlot()
            $('html, body').animate({
              scrollTop: $("#graph1").offset().top
          });  
        });
      }
});