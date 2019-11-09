from os import listdir, path
#   Fixed Lists    #
customers = []
datalist = []
final_dic = []

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
                    temporary_store['money']= money(customers[b])
                elif datalist [b][filename] == 'name':
                   temporary_store['name']= customer_name(customers[b])
                elif datalist [b][filename] == 'account':
                    temporary_store['account']= account(customers[b])
            if temporary_store in final_dic:
                temporary_store = {}
            else: 
                final_dic.append(temporary_store)
    return final_dic
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
        if len(l["money"]) > longest_money:
            longest_money = len(l["money"])

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
        diff_money = int(longest_money - len(data_stem[d]["money"]))

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
        column_money = symbol+padding_base +data_stem[d]["money"]+padding_money+ padding_base+symbol
        table +=  column_account + column_name + column_money+ "\n"
        total_lenght = int(len(column_account + column_name + column_money))
    return [table,total_lenght]
#   Transfers      #

#   Output         #
def output_file(content):
    

    #   Heading
    header = "Read from files:\n"
    
    #   Liner
    liner_symbol = ""
    for t in range(content[1]):
        liner_symbol += "*"
    liner_finish= liner_symbol +"\n"

    #   Writing
    if path.isfile('mini_project_3/data/output.txt') is False:
        f = open('mini_project_3/data/output.txt', 'w')
        f.write(header+liner_finish+content[0]+liner_finish)
        f.close()
        f = open('mini_project_3/data/output.txt', 'r')
        reader = f.read()
        f.close()
    else:
        f = open('mini_project_3/data/output.txt', 'r')
        reader = f.read()
        f.close()
    
    return reader
#   Run This       #
def run_it():
    return output_file(table(name_sorter(data_find(customer_find(directories())))))

print(run_it())

