  // var elem = document.querySelector('.collapsible');
  // var instance = M.Collapsible.init(elem, options);

  // Or with jQuery

  $(document).ready(function(){
    $('.collapsible').collapsible();





    $('select').formSelect();
		$(' select ').change(function() {
    		window.location = $(this).val();
		});

    });