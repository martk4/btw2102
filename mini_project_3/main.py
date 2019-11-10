from os import listdir, path
#   Fixed Lists    #
customers = []
datalist = []
final_dic = []
cleanest = []
header_theoutput = ""
header_new = "Round 1"
#   Readers        #
def money(name_dir):
    f = open("mini_project_3/data/"+name_dir+'/money', 'r')
    amount = f.read()
    f.close()
    return amount
def account(name_dir):
    g = open("mini_project_3/data/"+name_dir+'/account', 'r')
    account_numb = g.read()
    g.close()
    return account_numb
def customer_name(name_dir):
    h = open("mini_project_3/data/"+name_dir+'/name', 'r')
    name_cust = h.read()
    h.close()
    return name_cust
def full_file():
    f = open('mini_project_3/data/output.txt', 'r')
    reader_full = f.read()
    f.close()
    return reader_full
#   Data Finders   #
def directories():
    master_dir = listdir("mini_project_3")
    if "data" in master_dir:
        data_dir = sorted(listdir("mini_project_3/data"))
    else:
        print("Sorry, there seems to be no data available.")
    return data_dir
def customer_find(sub_dir):
    for a in range(len(sub_dir)):
        if "customer" in sub_dir[a]:
            customers.append(sub_dir[a])
    return customers
def data_find(customer_list):
    
    for files in range(len(customer_list)):
        datalist.append(listdir("mini_project_3/data/"+customer_list[files]))
        for b in range(len(datalist)):
            temporary_store= {}
            for filename in range(len(datalist[0])):
                if datalist[b][filename]== 'money':    
                    temporary_store['money']= int(money(customers[b]))
                elif datalist [b][filename] == 'name':
                   temporary_store['name']= customer_name(customers[b])
                elif datalist [b][filename] == 'account':
                    temporary_store['account']= account(customers[b])
            if temporary_store in final_dic:
                temporary_store = {}
            else: 
                final_dic.append(temporary_store)
    return final_dic
def file_splitter(a_file):
    #   Working Lists
    clean = []
    cleaner = []
    
    global header_theoutput
    #   Splitting File
    reading = a_file.split("*")
    for elm in range(len(reading)):
        if reading[elm] != "" and reading[elm] !="\n":
            clean.append(reading[elm])
    header = clean[0]
    header_theoutput = header.replace("\n","")
    clean.pop(0)
    #   Splitting List
    for i in range(0, len(clean), 3):
        cleaner.append(clean[i:i + 3])
    #   Pollish 
    for q in range(len(cleaner)):
        abc ="ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜÈÉÀabcdefghijklmnopqrstuvwxyzöäüàéèç.,-"
        temporary_dicti = {}
        the_name = ""
        temporary_dicti['account']=cleaner[q][0].replace(" ","")
        for letter in range(len(cleaner[q][1])):
            if cleaner[q][1][letter] in abc:
                the_name += cleaner[q][1][letter]
            elif cleaner[q][1][letter] == " " and cleaner[q][1][letter-1] in abc:
                the_name += cleaner[q][1][letter]
        temporary_dicti['name']=the_name[:-1]
        temporary_dicti['money']=int(cleaner[q][2].replace(" ",""))
        cleanest.append(temporary_dicti)
        
    return cleanest
#   Table Design   #
def name_sorter(to_sort):
    sorted_byname = sorted(to_sort, key=lambda k: k['name']) 
    return sorted_byname
def table(data_stem):
    #   Fixed Parameters
    table = ""
    longest_account = 0
    longest_name = 0
    longest_money = 0
     
    

    #   Length Finder
    for l in data_stem:
        if len(l["account"]) > longest_account:
            longest_account = len(l["account"])
        if len(l["name"]) > longest_name:
            longest_name= len(l["name"])
        if len(str(l["money"])) > longest_money:
            longest_money = len(str(l["money"]))

    #   Table Builder
    for d in range(len(data_stem)):
        # Changing Parameters
        symbol = "*"
        padding_base = " "
        padding_account = ""
        padding_name = ""
        padding_money= ""
        diff_account = int(longest_account - len(data_stem[d]["account"]))
        diff_name = int(longest_name - len(data_stem[d]["name"]))
        diff_money = int(longest_money - len(str(data_stem[d]["money"])))

    #   Space Adder
        for p in range(diff_account):
            padding_account += " "
        for q in range(diff_name):
            padding_name += " "
        for r in range(diff_money):
            padding_money += " "
    
    # Builder

        column_account = symbol+padding_base +data_stem[d]["account"]+padding_account+ padding_base
        column_name = symbol + padding_base +data_stem[d]["name"]+padding_name+ padding_base
        column_money = symbol+padding_base +str(data_stem[d]["money"])+padding_money+ padding_base+symbol
        table +=  column_account + column_name + column_money+ "\n"
        total_lenght = int(len(column_account + column_name + column_money))
    return [table,total_lenght]
#   Transactions      #
def change_header():
    global header_new 
    read_header = full_file()
    read_header = read_header.split("\n")
    read_header = read_header[0]
    if read_header == "Read from files:":
        read_header = 0
    else:
        read_header = read_header.split(" ")
        read_header = int(read_header[1])
        header_new = "Round "+str(read_header+1)

    return read_header
def transactions_read(): 
    global header_theoutput
    global header_new
    rounds= change_header()
    fol = directories() 
    transaction_dic = []
    for j in fol:
        if "transactions" in fol:
            f = open('mini_project_3/data/transactions', 'r')
            transacts = f.read()
            f.close()
        elif "transactions" not in fol:
            print("Sorry, there seems to be no transactions today")
    transaction_list = transacts.split("\n")

    for full_info in transaction_list:
        temp_dic = {}
        temp_trans = full_info.split(",")
        temp_dic['sender'] = temp_trans[0]
        temp_dic['reciever'] = temp_trans[1]
        temp_dic['amount'] = temp_trans[2]
        transaction_dic.append(temp_dic)
    return transaction_dic[rounds]
def transactions_book():
    case = transactions_read()
    for tutto in range(len(cleanest)):
        if case["sender"] == cleanest[tutto]["account"]:
            cleanest[tutto]['money'] -= int(case["amount"])
        if case["reciever"] == cleanest[tutto]["account"]:
            cleanest[tutto]['money'] += int(case["amount"])
    return case
#   Output         #
def output_file_first(content):
    #   Heading
    header = "Read from files:\n"
    #   Liner
    liner_symbol = ""
    for t in range(content[1]):
        liner_symbol += "*"
    liner_finish= liner_symbol +"\n"
    #   Writing
    f = open('mini_project_3/data/output.txt', 'w')
    f.write(header+liner_finish+content[0]+liner_finish)
    f.close()
    f = open('mini_project_3/data/output.txt', 'r')
    reader = f.read()
    f.close()
    return reader
def output_file_following(content):
    global header_new
    #   Heading
    header = header_new
    #   Liner
    liner_symbol = ""
    for t in range(content[1]):
        liner_symbol += "*"
    liner_finish= liner_symbol +"\n"
    #   Writing
    f = open('mini_project_3/data/output.txt', 'w')
    f.write(header+"\n"+liner_finish+content[0]+liner_finish)
    f.close()
    f = open('mini_project_3/data/output.txt', 'r')
    reader = f.read()
    f.close()
    return reader
#   Run This       #
def run_it():
    if path.isfile('mini_project_3/data/output.txt') is False:
        final_output = output_file_first(table(name_sorter(data_find(customer_find(directories())))))
    else:
        file_splitter(full_file())
        try:
            transactions_book()
            final_output= output_file_following(table(cleanest))
        except IndexError:
            final_output = "Sorry, there seems to be no more transactions"
    return final_output
print(run_it())