from Manager import Manager as mg
from Developer import Developer as dev
from Employee import Employee as emp
from Utility import Utility as ut

if __name__ == "__main__":

    # e = emp("Vittal", "500000000")

    # e1 = emp("Govinda", "4561239874")

    # dev = dev("Gouri", "4561239", "py")

    # mg1 = mg("datta", "4578984", "c++")

    # mg1.add_employee(e)

    # mg1.add_employee(e)

    # mg1.add_employee(e)

    # # print(mg1._employees[0]._name)

    # mg_new  = mg("guru", "123456", "py")

    # mg_new.add_employee(e1)
    # mg_new.add_employee(e1)
    # mg_new.add_employee(e1)

    # mg3 = mg("Krishna", "4578", "cpp")

    # ob = ut.print_employees_under_each_manager([mg1, mg_new, mg3])

    # mg_list = [mg1, mg_new, mg3]
    # i = 0

    menu = '''Menu
1)Employee
2)Developer

Enter choice'''
    m1 = mg("Arun")
    m2 = mg("Deva")
    m3 = mg("Babu")
    m4 = mg("Chandru")

    m_list = [m1, m3, m4, m2]

    while True:
        print(menu)

        c = int(input())

        if c == 1:
            print("Enter Employee details in comma separated format")

            d = input().split(',')
            d[1] = int(d[1])

            print("Enter manager name")

            m_name = input()

            e = emp(d[0], d[1])

            if m_name == "Babu":
                m3.add_employee(e)
            elif m_name == "Arun":
                m1.add_employee(e)
            elif m_name == "Deva":
                m2.add_employee(e)
            else:
                m4.add_employee(e)

            print("Do you want to continue? Type yes/no")
            res = input()

            if res == "yes":
                continue
            else:
                ob = ut.print_employees_under_each_manager(m_list)
                print()
                print("Manager and Employee Allocation List")
                print()
                print()

                i = 0
                

                for ele in ob:

                    print(f"Manager Name :{m_list[i].name}")
                    print("Employee List :")

                    if len(ele) == 0 or not ele:
                        print(None)

                    for e in ele:
                        print(e._name, end=" ")
                    print()
                    print()

                    i = i+1
                break
        else:
            print("Enter Developer details in comma separated format")

            d = input().split(',')
            d[1] = int(d[1])

            print("Enter manager name")

            m_name = input()

            dev_obj = dev(d[0], d[1], d[2])

            if m_name == "Babu":
                m3.add_employee(dev_obj)
            elif m_name == "Arun":
                m1.add_employee(dev_obj)
            elif m_name == "Deva":
                m2.add_employee(dev_obj)
            else:
                m4.add_employee(dev_obj)

            print("Do you want to continue? Type yes/no")
            res = input()

            if res == "yes":
                continue
            else:
                ob = ut.print_employees_under_each_manager(m_list)
                i = 0
                print()
                print("Manager and Employee Allocation List")
                print()
                print()

                
                for ele in ob:

                    print(f"Manager Name :{m_list[i].name}")
                    print("Employee List :")

                    if len(ele) == 0 or not ele:
                        print(None)

                    for e in ele:
                        print(e._name, end=" ")

                    print()
                    print()

                    i = i+1
                break
