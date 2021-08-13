$(function(){
    $("#rtt").on('keypress', function(event){
        key  = event.originalEvent.key;
        console.log(key);
        ttsSocket.send(JSON.stringify({'msg': key}));        
    })
    let navel = $(".nav-link")
    let ul = $("ul.bxslider")
    navel.click(function(){
        $(".nav-link").removeClass("active");
        $(this).addClass("active");
        index = $(this).parent().index();
        $(".bx-pager-item a")[index].click();
    })
    $('.bxslider').bxSlider({
        onSlideBefore: function(a, b, c){
            navel[c].click()
            console.log(b)
            $(ul.children().not(".bx-clone")[b]).find("textarea, button, a").blur()
        },
        
        onSliderLoad: function(a){
            navel[a].click()
        }
    });
    const ttsSocket = new WebSocket(
                    'ws://'
                    + window.location.host
                    + '/ws'
                    + '/rtt'
                    + '/'
                );    
    var socketMessage = function(msg) {
        const data = JSON.parse(msg.data);
    };
    ttsSocket.onmessage = socketMessage
})