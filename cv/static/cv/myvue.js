new Vue({
    el: 'form',
    methods: {
        changeTextSize: function(event) {
            if (event.target.value) {
                event.target.style.textAlign = 'center';
                event.target.style.backgroundColor = 'red';
            }
        },
        changeColor: function(event) {
            event.target.style.backgroundColor = "orange"
        }
    }
})

// function changeTextSize(ele) {
//     ele.style.textAlign = 'center';
//     ele.style.fontSize = 'xx-large';
// }

// new Vue({
//     el: '#input',
//     methods: {
//         resizeInput: function(event) {
//             if (event.key == 'Enter')
//         }
//     }
// })

// var app5 = new Vue({
//     delimiters: ['[[', ']]'],
//     el: '#input-one',
//     data: {
//         message: 'abcde'
//     },
//     methods: {
//         reverseMessage: function () {
//             this.message = this.message.split('').reverse().join('')
//         }
//     }
// })
// var example2 = new Vue({
//     el: '#title-input',
//     // define methods under the `methods` object
//     methods: {
//       changeCursor: function (event) {
//         document.getElementById("title-input").style.cursor = "pointer";
//         // // `this` inside methods points to the Vue instance
//         // alert('Hello ' + this.name + '!')
//         // // `event` is the native DOM event
//         // if (event) {
//         //   alert(event.target.tagName)
//         // }
//       }
//     }
//   })

//   function changeInput(ele) {
//     if(event.key === 'Enter') {
//         ele.style.fontSize = 'xx-large';
//         ele.style.textAlign = 'center'
//     }
// }

  