// OOP in JS

class Person {
    constructor(name, age){
        this.name = name
        this.age = age
    }

    teach(){
        console.log(`${this.name} teaches`)
    }
}

const alex = new Person("Alex", 37)

console.log(alex.name, alex.age)
alex.teach()