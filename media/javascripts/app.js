(function($) {
	$().ready(function() {
		// Django CSRF protection for AJAX requests. Omnomnom
		$('html').ajaxSend(function(event, xhr, settings) {
			function getCookie(name) {
				var cookieValue = null;
				if (document.cookie && document.cookie != '') {
					var cookies = document.cookie.split(';');
					for (var i = 0; i < cookies.length; i++) {
						var cookie = jQuery.trim(cookies[i]);
						// Does this cookie string begin with the name we want?
						if (cookie.substring(0, name.length + 1) == (name + '=')) {
							cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							break;
						}
					}
				}
				return cookieValue;
			}
			if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				// Only send the token to relative URLs i.e. locally.
				xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			}
		});
		
		/* Auto-expand all textareas */
		var textareaIntervalTimer;
		$('textarea').live('focusin focusout', function(event) {
			if (event.type === 'focusout') {
				clearInterval(textareaIntervalTimer);
			}
			
			if (event.type === 'focusin') {
				var text = $(textarea).val(),
				textarea = this;
				textareaIntervalTimer = setInterval(function() {
					if (text === $(textarea).val()) {
						return;
					}
					
					text = $(textarea).val();
					
					var lines = (((text.length) - (text.length % 60)) / 60) + 2,
					multiplier = $(textarea).css('line-height') || 1;
					
					$(textarea).css({
						height: (lines * parseInt(multiplier)) + 'px'
					});
				}, 750);
			}
		});
	});
})(jQuery);
