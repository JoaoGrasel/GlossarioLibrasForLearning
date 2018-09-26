 $(document).ready(function() {
    $("#MostrarEsconderMensagem").click(MostrarEsconderMensagem);
 });
 
        
function MostrarEsconderMensagem(){
    $("#Mensagem").toggle();
}


$('#glossario').mousemove(function(){
    $(this).attr('src','../imagens/glossario.jpg');
});

$(function(){  
    $("#glossario").hover(
        function(){$(this).attr("src", "../../static/Glossario/imagens/glossario.jpg")},
        function(){$(this).attr("src", "../../static/Glossario/imagens/glossario1.jpg")}
    );

     $("#pasta").hover(
        function(){$(this).attr("src", "../../static/Glossario/imagens/pasta.jpg")},
        function(){$(this).attr("src", "../../static/Glossario/imagens/pasta1.jpg")}
    );


});


 
