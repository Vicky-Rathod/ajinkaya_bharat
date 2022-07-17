(function(window){

var supportedWebP = null,
	webPPrefix = window.location.protocol + '//webpcache.epapr.in/index.php?in=',
	webPPrefixV2 = 'https://icdn.readwhere.com/size/default/format/webp/src/',
	webPEnable = ( typeof DEConfig != 'undefined' && typeof DEConfig.webPEnable != 'undefined' ) ? DEConfig.webPEnable : false,
	events = {
		webPSupportChecked: 'webPSupportCheckedEvent',
		contentLoaded: 'contentLoadedEvent'
	};


var ENC = {
  '+': '-',
  '/': '_',
  '=': '.'
};


var detectWebPSupport = function() {

  if ( supportedWebP != null ) {

  	$( window ).trigger( events.webPSupportChecked );
    return;
  }

  var webP = new Image();
  webP.onload = function() {

    supportedWebP = (webP.height === 2) ? true : false;
    $( window ).trigger( events.webPSupportChecked );
  }
  webP.onerror = function() {

    supportedWebP = false;
    $( window ).trigger( events.webPSupportChecked );
  }
  webP.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
}

var getImageUrl = function( url ) {
	
	if ( !webPEnable || !supportedWebP ) {

		return url;
	} else {

		return webPPrefix + url;
		
		/*if( DEConfig.hasOwnProperty('webPVersion') && DEConfig.webPVersion == 2 ) {

			return webPPrefixV2 + btoa(url.replace('http:','https:')).replace(/[+/=]/g, function(match){ return ENC[match];});
		} else {

			return webPPrefix + url;
		}*/
	}
}

var loadImages = function() {

	$( "img[data-src]" ).each( function( index, img ) {
		
		if ( typeof $.fn.unveil != 'function' ) {

			$( img ).load( function() {

				$( img ).removeAttr( 'data-src' );
			});
			$( img ).attr( 'src', getImageUrl( $(img).attr( 'data-src' ) ) );
		} else {

			$( img ).attr( 'data-src', getImageUrl( $(img).attr( 'data-src' ) ) );
		}
	});

	if ( typeof $.fn.unveil == 'function' ) {

		$( "img[data-src]" ).unveil(0, function() {

			$( this ).removeAttr( 'data-src' );
		});

		//code for IE compatibility for unveil
		setTimeout( function() {
			$( window ).scroll();
		}, 2000 );
	}
}

$(document).ready( function() {

	detectWebPSupport();

	$( window ).bind( events.webPSupportChecked, loadImages );
	$( window ).bind( events.contentLoaded, detectWebPSupport );
})

window.webPLoadExists = true;
window.webPGetImageUrl = getImageUrl;
})(window);