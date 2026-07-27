////////////////////////////////////////////
;(function (packageFunction) {
  /* istanbul ignore next */
  var p = window.AmazonUIPageJS || window.P;
  /* istanbul ignore next */
  var attribute = p._namespace || p.attributeErrors;
  /* istanbul ignore next */
  var namespacedP = attribute ? attribute("BotDetectionJSSignalCollectionAsset", "") : p;

  /* istanbul ignore next */
  if (namespacedP.guardFatal) {
    namespacedP.guardFatal(packageFunction)(namespacedP, window);
  } else {
    namespacedP.execute(function () {
      packageFunction(namespacedP, window);
    });
  }
}(function(P, window, undefined){
// BEGIN ASSET BotDetectionJSSignalCollectionAsset - 1.0
/////////////////////////
// BEGIN FILE rxlang-loader.js
/////////////////////////
/*


Full source (including license, if applicable) included below.
*/
(function () {
    'use strict';
    
    var eventHandlers = {};
    var emittedEvents = {};

    window._bcxp = {
        DEBUG: 0,
        e: function(eventName, value) {
            emittedEvents[eventName] = value;
            var handlers = eventHandlers[eventName] || [];
            var i;
            for (i = 0; i < handlers.length; i = i + 1) {
                handlers[i](value);
            }
        },
        r: function(eventName, handler) {
            if (typeof handler !== 'function') {
                return;
            }
            if (!eventHandlers[eventName]) {
                eventHandlers[eventName] = [];
            }
            eventHandlers[eventName].push(handler);
            
            // If event was already emitted, call handler immediately
            if (eventName in emittedEvents) {
                handler(emittedEvents[eventName]);
            }
        }
    };

    if (_bcxp.DEBUG) {
        console.log('Loading..');
    }
    
    try {
        rx.ex64("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", "load");

        rx.ex64("UlgBKS4mS0pSJ0ZJJ1BAJlZMQSZXTEEsQ1JGTEhhRFFEL0ZQVlFKSEBXbEEhUEBVUS1VREJAcVxVQC1JSkZEUUxKSyxQVkBXZEJAS1EkJBUpIWFEUUAFJSQnFSkjUkxLQUpSBSUkJhUpLEtEU0xCRFFKVwUlJCEVKSB6R0ZdVQUlFRUoJQUkJCAkJCMzFRUpIUJWVkIFISQiJBUVKSdCQAUhLhcVKCQFIRcpOWdKUWZ9BWhAUVdMRlYFCAVgS1NMV0pLSEBLUR8XFSgkBSEFIikGZ0pRZn0FaEBRV0xGVgUIBXZQVk1MBXZKUFdGQAViV0pQVR9kLdQkta+vkp++no6+mp6enp6enJSem5SjA6+SnK+Snb6dr5Kdvp2Vn56cr5Kcr5Kdvp2jA6+Sm6+Snb6dr5Kdvp2Vn56br5Kbr5Kdvp2empSjA6+Sma+Smr6dA6+Smr6dAb+asJ+emq+Sma+Smr6dra+Snr6bv5qThNzq7Ovw8vrtv9bbv/nt8PK/+ej89vLb/uv+paMBv5qsn66vkp6+m5O03Ors6/Dy+u2/1tu/8fDrv/nw6vH7v/bxv/7x5r/08fDo8b/z8Pz+6/bw8Z6ZlKMDr5KXr5KYvp2vkpi+nbefnpmvkpevkpi+na2vkp6+m7+Zk4vP/vj6v8vm7/q/+e3w8r/q+u/rpa+vkp++npSqvp6tnK+TlOvw1szQzOvt9vH4nq+elK+vk5r46v756b6blJyIkb+ek5Ds+uzs9vDx2+rt/uv28PG+mpOM/PDz8/r86/bw8czr/u3ry/by+q+Tm/ft+vmvkpa+nZOc6u3zrZOS6v7Z6vPzyfrt7Pbw8a+Slb6ckpWvk5f38Ozr8f7y+q+Slr6dk5n78PL+9vGtk5br9vL67Ov+8u+enZ6jv5yPn5u/nJOW7Prs7Pbw8db7v52jv5uPn5u/m5OW7fru6vrs69b7v52jv5qYn5u/mpKZv52jv5mYn5u/mZKXv52yv51kLFIls5qZm4+cuJqUnPz57Pm4mZSS9f3s6vH7zOHo/ai5kJmcmZmej5q4m5SQ/fT99f327OupqJSb/ev8uZy4npmfmZmdj5y4n5SW+fz88ezx9/b59Nz57Pm4nJSX6/3r6/H39tX97Pn8+ez5qqiUm+vs67mcuZ+4nbQhBS0pJlZIQQUhIQUsKSRIBSE=", "load");

        rx.ex64("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", "load");

        rx.ex64("UlgBJCQVKSB6R0ZdVQUlFRUpJ0JABSQkJyRkJn8laUJA009HbSQhLtNiQU9ZICwubSIuIjksLW0BLDcAGxMsLyogOm0tIm1zc09AMC4nYkJCQkJCQVRBY0JPTDAmMDAqLC0OJjciJyI3InFzT0AwNzBiQmNAY0FvIQUmKSZCR0gFJA==", "load");

        if (_bcxp.DEBUG) {
            console.log('Loaded successfully');
        }
        
        if (document.readyState === 'complete' || document.readyState === 'interactive') {
            _bcxp.e("load");
        } else {
            document.addEventListener('DOMContentLoaded', function() {
                _bcxp.e("load");
            });
        }
    
    } catch (error) {
        if (_bcxp.DEBUG) {
            console.error('Error loading..: ', error);
        }
        throw error;
    }
    
})();
/////////////////////////
// END FILE rxlang-loader.js
/////////////////////////
// END ASSET BotDetectionJSSignalCollectionAsset - 1.0
}));
////////////////////////////////////////////