function loadBox(clas,iW,iH,w,h,ifr)
{
	 
     $("."+clas).colorbox({
          iframe:ifr,
          innerWidth:iW,
          height:iH,
          //initialWidth:w,
          //initialHeight:h,
          scrolling:false,
          onComplete : function() {   
               if(ifr)
               {    var iframeHeight= '"'+$("#cboxLoadedContent").height()+'px"';
                    $("#cboxLoadedContent").height(iframeHeight);
               }
                  
          }
          ,
          onClosed:function(){
        	   
               //location.reload(false);
          }
     });

}
var next="";
function closeBox()
{$(".close").click(function(){
	$.colorbox.close();
});}