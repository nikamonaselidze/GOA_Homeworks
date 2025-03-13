function elimination(arr) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j]) {
                return arr[i]
            }
        }
    }
    return null
}

// Is that a real phone number? (British version)

function validateNumber(str){
  
    let avg = str.split("-").join("")
    if(avg.slice(0,2)== "07" && avg.length == 11){
      return "In with a chance"
    }
    
    if(avg.slice(0,3) == "+44" && avg.length == 13){
      return "In with a chance"
    }
    
    return 'Plenty more fish in the sea'
  
  }

// countCharOccurrences

function countCharOccurrences(s, char) {
    return s.split(char).length - 1
}