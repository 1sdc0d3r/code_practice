const pets = [
  {
    name: "Tinkerbell",
    species: "cat",
    age: 2
  },
  {
    name: "Lucy",
    species: "dog",
    age: 12
  },
  {
    name: "Chloe",
    species: "cat",
    age: 18
  },
  {
    name: "Mojo",
    species: "dog",
    age: 6
  },
  {
    name: "Olivia",
    species: "parakeet",
    age: 4
  },
  {
    name: "Shadow",
    species: "cat",
    age: 8
  },
  {
    name: "Oreo",
    species: "cat",
    age: 5
  },
  {
    name: "Molly",
    species: "dog",
    age: 4
  },
  {
    name: "Freddie Prinze Jr.",
    species: "parakeet",
    age: 9
  }
];

let speciesArr = [];

function sumPetYears(arr, kind, multiply) {
  speciesArr = arr.filter(function(arr) {
    return arr.species == kind;
  });
  let ages = speciesArr.map(function(eachAge) {
    return eachAge.age * multiply;
  });
  ageTotal = ages.reduce(function(acc, cv) {
    return acc + cv;
  }, 0);
  return ageTotal;
}

console.log(sumPetYears(pets, "dog", 5));

// map filter reduce
const fixMe = (arr, kind, multiply) => {
  const weDidIt = arr
    .filter(item => {
      return item.species === kind;
    })
    .map(item => {
      return item.age * multiply;
    })
    .reduce((acc, next) => {
      return acc + next.age;
    }, 0);
  return weDidIt;
};

console.log(sumPetYears(pets, "dog", 3));

//todo .filter out all specified species
//todo map out ages in new array
//todo multiply by argument(num)
//todo .reduce all to one number
