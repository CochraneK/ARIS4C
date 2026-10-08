jQuery(function($) {
    $(".animals_calculate_form #species1").on( 'change', function(event){ 
        var species = $(this).val();
        if( species != '' ){
            $(this).removeClass('error');

            var lower_ranger = $(this).find("option:selected").data('min');
            var higher_ranger =  $(this).find("option:selected").data('max');

            $(".animals_calculate_form #x_value").attr('min',lower_ranger).attr('max',higher_ranger);
            $(".animals_calculate_form #low_ranger").val( lower_ranger );
            $(".animals_calculate_form #high_ranger").val( higher_ranger );
            $(".animals_calculate_form #minn").html( lower_ranger );
            $(".animals_calculate_form #maxx").html( higher_ranger );
        } else {
            $(".animals_calculate_form #x_value").attr('min',0).attr('max',0);
            $(".animals_calculate_form #low_ranger").val(0);
            $(".animals_calculate_form #high_ranger").val(0);
            $(".animals_calculate_form #minn").html('-');
            $(".animals_calculate_form #maxx").html('-');
        }
    });

    $(".animals_calculate_form #species2").on( 'change', function(event){ 
        var species = $(this).val();
        if( species != '' ){
            $(this).removeClass('error');
        }
    });

    $(".animals_calculate_form #process").on( 'change', function(event){ 
        var processs = $(this).val();
        if( processs != '' ){
            $(this).removeClass('error');
        }
    });

    $(".animals_calculate_form #location").on( 'change', function(event){ 
        var location = $(this).val();
        if( location != '' ){
            $(this).removeClass('error');
        }
    });

    $(".animals_calculate_form #x_value").on( 'change', function(event){ 
        var x_value = $(this).val();
        if( x_value > 0 ){
            $(this).removeClass('error');
        }
    });

    $(".humans_calculate_form #humans_calculate").on( "click", function() {

        var xday = $(".humans_calculate_form #x_day").val();

        var have_error = false;

        if ( '' == xday ) {
            have_error = true;
            $(".humans_calculate_form #x_day").addClass('error');
        }

        if ( ! have_error ) {

            jQuery.post(
                calculation_days_sepcies_var.ajax_url, 
                {
                    'action': 'calculation_days_sepcies_action',
                    'method': 'calculate_day_humans',
                    'xday'  : xday,
                }, 
                function(response){
                    $(".humans_calculate_form .show_result").html( response );
                }
            );
        }
        return false;
    });
    
    $(".animals_calculate_form #submit_calculate").on( "click", function() {
        var species1 = $(".animals_calculate_form #species1").val();
        var species2 = $(".animals_calculate_form #species2").val();
        var processs = $(".animals_calculate_form #process").val();
        var location = $(".animals_calculate_form #location").val();
        var low = parseFloat( $(".animals_calculate_form #low_ranger").val() );
        var high = parseFloat( $(".animals_calculate_form #high_ranger").val() );
        var day_x = parseFloat( $(".animals_calculate_form #x_value").val() );

        var have_error = false;

        if ( '' == species1 ) {
            have_error = true;
            $(".animals_calculate_form #species1").addClass('error');
        }

        if ( '' == species2 || species1 == species2 ) {
            have_error = true;
            $(".animals_calculate_form #species2").addClass('error');
        }

        if ( '' == processs ) {
            have_error = true;
            $(".animals_calculate_form #process").addClass('error');
        }

        if ( '' == location ) {
            have_error = true;
            $(".animals_calculate_form #location").addClass('error');
        }

        if ( isNaN(day_x) || day_x < 1 || day_x < low || day_x > high ) {
            have_error = true;
            $(".animals_calculate_form #x_value").addClass('error');
        }

        if ( ! have_error ) {

            jQuery.post(
                calculation_days_sepcies_var.ajax_url, 
                {
                    'action': 'calculation_days_sepcies_action',
                    'method': 'calculate_day_pet',
                    'species1': species1,
                    'species2': species2,
                    'processs': processs,
                    'location': location,
                    'day_x': day_x,
                    'low_ranger': low,
                    'high_ranger': high,
                }, 
                function(response){
                    $(".animals_calculate_form .show_result").html( response );
                    console.log(response);
                }
            );
        }

        return false;
    });
});