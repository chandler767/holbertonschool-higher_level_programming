
class Person { // create a class 'person' and assign from main file
  var first_name: String
  var last_name: String
  var age: Int

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  }

  func fullName() -> String {
    return "\(self.first_name) \(self.last_name)" // return first name and last name joined by a space
  }

}

class Student: Person, Classify {
  func isStudent() -> Bool {
    return true  // Student is a student so return true
  }
}

enum Subject { // subjects 
  case Math
  case English
  case French
  case History
}

protocol Classify {
  func isStudent() -> Bool // returns true or false based on person type. See isStudent() below.
}

class Mentor: Person, Classify { // sub class for mentors 
  let subject: Subject
  // overloading constructor
  init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
    self.subject = subject
    super.init(first_name: first_name, last_name: last_name, age: age)
  }

  func stringSubject() -> String {
    switch subject { // get the subject and return as a string
      case .Math: return "Math"
      case .English: return "English"
      case .French: return "French" //
      case .History: return "History"
    }
  }

  func isStudent() -> Bool {
    return false // not a student - return false
  }

}

// class school where Person (student or mentor) can be added to
class School {
  var name: String
  var list_persons: [Person]
  init(name: String) {
    self.name = name
    self.list_persons = [] // Create the class school with a list of persons.
  }

  func addMentor(p: Person) -> Bool {
    if p is Mentor {
      list_persons.append(p)
      return true // if p is a mentor add to the list
    } else {
      return false
    }
  }

  func addStudent(p: Person) -> Bool {
    if p is Student {
      list_persons.append(p)
      return true // if p is a student add to the list
    } else {
      return false
    }
  }
  
   func listMentors() -> [Person] {
    var mentors: [Person] = []
    for person in list_persons {
      if person is Mentor { 
        mentors.append(person) // add all mentors to a list
      }
    }
    return mentors.sort {
      $0.age < $1.age // sort by age
    }
  }

  func listStudents() -> [Person] { // same as list mentors but with students
    var students: [Person] = []
    for person in list_persons {
      if person is Student { 
        students.append(person) // add all students to a list
      }
    }
    return students.sort {
      $0.age < $1.age // sort by age
    }
  }



  func listMentorsBySubject(subject: Subject) -> [Person] { // same as list mentors but with subject used
    var mentors: [Person] = []
    for person in list_persons {
      if person is Mentor {
        if let mentor = person as? Mentor {
          if mentor.subject == subject { // does mentor.subject equal the subject in main
            mentors.append(mentor) // add mentors to a list
          }
        }
      }
    }
    return mentors.sort {
      $0.age < $1.age // sort by age
    }
  }
}
