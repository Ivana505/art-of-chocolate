var updateBtns = document.getElementsByClassName('update-basket')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var chocolateId = this.dataset.chocolate;
        var action = this.dataset.action;
        console.log('chocolateId:', chocolateId, 'action:', action)

        console.log('USER', user);
        if (user == 'AnonymousUser') {
            addCookieItem(chocolateId, action)
        }else {
            updateUserOrder(chocolateId, action)
        }
    })
}


// function addCookieItem(chocolateId, action) {
//     console.log('You are not logged in')

//     if (action == 'add') {
//         if(basket[chocolateId] == undefined){
//             basket[chocolateId] = {'quantity':1}
//         }else{
//             basket[chocolateId]['quantity'] += 1
//         }
//     }

//     if (action == 'remove') {
//         basket[chocolateId]['quantity'] -= 1

//         if (basket[chocolateId]['quantity'] <= 0) {
//             console.log('Remove Item')
//             delete basket[chocolateId];
//         }
//     }
//     console.log('Basket', basket)
//     document.cookie = 'basket=' + JSON.stringify(basket) + ";domain=;path=/"
//     location.reload()
// }


function updateUserOrder(chocolateId, action) {
    console.log('You are logged in, processing data...')

    var url = '/update_item/'

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
            return response.json()
        })
    .then((data) => {
            console.log('data', data)
            location.reload()
        })

}