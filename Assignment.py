class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self) -> None:
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = new_node 
    
    

class Product:#tree
    def __init__(self,pcode,pname,quan,sa,p) -> None:
        self.pcode = pcode
        self.proname = pname
        self.quantity = quan
        self.saled = sa
        self.price = p

class Customer:#linked list
    def __init__(self,ccode,cus_name,phone) -> None:
        self.ccode = ccode
        self.cus_name = cus_name
        self.phone = phone
class Ordering: #linked list
    def __init__(self,pcode,ccode,quan) -> None:
        self.pcode = pcode
        self.ccode = ccode
        self.quantity = quan
class Product_List:
    def __init__(self) -> None:
        self.lst_Product = Linked_list()
        print("1.1.      Load data from file \n1.2.      Input & insert data \n1.3.      In-order traverse \n1.4.      Breadth-first traverse \n1.5.      In-order traverse to file \n1.6.      Search by pcode \n1.7.      Delete by pcode by copying \n1.8.      Simply balancing \n1.9.      Count number of products")
        input_choice = input('Choice: ')
    
    def f1_2(self):
        inp_pcode = input('Enter pcode: ')
        inp_pname = input('Enter proname: ')
        inp_quan = input('Enter quantity: ')
        inp_sa = input('Enter saled: ')
        inp_p = input('Enter price: ')
        new_product = Product(inp_pcode,inp_pname,inp_quan,inp_sa,inp_p)
        self.lst_Product.push(new_product)

    def f1_3(self):
        pass

class Customers_list:
    def __init__(self) -> None:
        print('2.1.      Load data from file\n2.2.      Input & add to the end\n2.3.      Display data\n2.4.      Save customer list to file\n2.5.      Search by ccode\n2.6.      Delete by ccode')
        input_choice = input('Choice: ')


class Order_list:
    def __init__(self) -> None:
        self.lst_order = Linked_list()
        print('3.1.      Input data\n3.2.      Display ordering data\n3.3.      Sort by pcode + ccode')
        input_choice = input('Choice: ')
        
    
    def f3_1(self): 
        inp_pcode = input('Enter pcode: ')
        inp_ccode = input('Enter pcode: ')
        inp_quan = input('Enter pcode: ')
        new_order = Ordering(inp_pcode,inp_ccode,inp_quan)
        self.lst_order.push(new_order)

    def f3_2(self):
        curr_node = self.lst_order.head
        while(curr_node.next != None):
            print(curr_node.data.pcode,' ',curr_node.data.ccode,' ',curr_node.data.quan)
            curr_node = curr_node.next
    
    def f3_3(self):
        
        


class App:
    def __init__(self) -> None:
        pass
    def main(self):
        print('. Product \n2.Customers_list \n3.Order_list')
        input_choice = input('Choice: ')
a = App()
a.main()
