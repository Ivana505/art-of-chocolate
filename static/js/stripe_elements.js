// var stripe_public_key = $('#id_script_public_key').text().slice(1, -1);
// var stripe_client_secret = $('#id_client_secret').text().slice(1, -1);
// var stripe = Stipre(stripe_public_key);
// var elements = stripe.elements();
// var card = element.create('card');
// card.mount('#card-element');

// card.addEventlistener('change', function (event) {
//     var errorDiv = document.getElementById('card-errors');
//     if (event.error) {
//         var html = 
//             <span class="icon" role="alert">
//                 <i class="fas fa-times"></i>
//             </span>
//             <span>${event.error.message}</span>
//         ;
//         $(errorDiv).html(html);
//     }else {
//         errorDiv.textContent = '';
//     }
// })