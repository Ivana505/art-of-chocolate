/* jshint esversion: 11, jquery: true */

var updateBtns = document.getElementsByClassName('update-basket');

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var chocolateId = this.dataset.chocolate;
        var action = this.dataset.action;
        console.log('chocolateId:', chocolateId, 'action:', action);

        console.log('USER', user);
        if (user == 'AnonymousUser') {
            if (action=="add"){
                if (basket[chocolateId]==undefined){
                    basket[chocolateId]={
                        "quantity":1
                    };
                }else
                {
                    basket[chocolateId]["quantity"]+=1;
                }
            }
            if (action=="remove"){
                basket[chocolateId]["quantity"]-=1;
                if(basket[chocolateId]["quantity"]<=0){
                    delete basket[chocolateId];
                }
            }
            console.log(basket);
            document.cookie="basket="+JSON.stringify(basket)+";domain=;path=/";
            location.reload();
        }else {
            updateUserOrder(chocolateId, action);
        }
    });
}

function updateUserOrder(chocolateId, action) {
    console.log('You are logged in, processing data...');

    var url = '/update_item/';

    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'chocolateId': chocolateId,
                'action': action
            })
        })

    .then((response) => {
            return response.json();
        })
    .then((data) => {
            console.log('data', data);
            location.reload();
        });

}

 //Thanks to channel https://www.youtube.com/watch?v=g_5ZDrl2KKE for creating this function to restrict letter input into input field//
function restrictAlphabets(e){
    var x = e.which || e.keycode;
    if((x >= 48 && x <=57))
        return true;
    else
        return false;
}


let user = '{{request.user}}';
         
function getToken(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getToken('csrftoken');


function getCookie(name) {
   var cookieArr = document.cookie.split(";");

   for(var i = 0; i < cookieArr.length; i++) {
       var cookiePair = cookieArr[i].split("=");

       if (name == cookiePair[0].trim()) {
          return decodeURIComponent(cookiePair[1]);
    }
  }
  
  return null;
}

var basket = JSON.parse(getCookie('basket'));
if (basket == undefined){
    basket = {};
    console.log('Basket was created', basket);
    document.cookie = 'basket=' + JSON.stringify(basket) + ";domain=;path=/";
   }
console.log('basket:', basket);


