#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int get();
		void set(int);
		int Fib();		
	private:
		int age;
		int Fib_pr(int);		
	};
 
Person::Person(int n){
	age = n;
	}
 
int Person::get(){
	return age;
	}
 
void Person::set(int n){
	age = n;
	}
int Person::Fib_pr(int n){
	if (n <= 1){
		return n;
	}
	return fib(n - 1) + fib(n - 2);
}

int Person:: Fib(){
	return Fib_pr(age);
}
extern "C"{
	Person* Person_new(int n) {return new Person(n);}
	int Person_get(Person* person) {return person->get();}
	void Person_set(Person* person, int n) {person->set(n);}
	int Person_Fib(Person* person) {return person->Fib();}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}