class Animal {
    constructor(leg_count, nutrition, habitat, age, name, sex) {
        this.leg_count = leg_count,
        this.nutrition = nutrition,
        this.habitat = habitat,
        this.age = age,
        this.name = name,
        this.sex = sex
    }

    eat(a) {
        return `${this.name} is eating ${a}`;
    } 
}

const harambe1 = new Animal(2, "herbivore", "forest", 17, "Harambe", "male");


function print_details(emna) {
    for (const [key, value] of Object.entries(emna)) {
        console.log(`${key}: ${value}`);
    }

    // console.log(`Name: ${harambe1.name}`);
    // console.log(`Age: ${harambe1.age}`);
    // console.log(`Sex: ${harambe1.sex}`);
    // console.log(`Leg Count: ${harambe1.leg_count}`);
    // console.log(`Nutrition: ${harambe1.nutrition}`);
    // console.log(`Habitat: ${harambe1.habitat}`);
    // console.log(harambe1.eat("bananas"));
}

print_details(harambe1);
