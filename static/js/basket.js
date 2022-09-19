var updateBtns = document.getElementsByClassName('update-basket')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var chocolateId = this.dataset.chocolate
        var action = this.dataset.action
        console.log('chocolateId:', chocolateId, 'action:', action)

        console.log('USER', user)
        if(user === 'AnonymousUser'){
            console.log('You are not logged in')
        }else{
            console.log('You are logged in, processing data...')
        }

    })
}