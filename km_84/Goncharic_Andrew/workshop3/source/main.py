"""
Тут написати умову до завдання
"""

work_plan = [
    {"master_name":"jon",
    "work_diary":[

                {
                    "adress": "metalistiv 3",
                    "task" : ["break crane",'change windows','connect to internet'],
                    "requirement": {"key of 18","otvertka","paialnmik"},
                    "requirement time": "10:00 AM"
                },

                {
                    "adress": "metalistiv 7",
                    "task" : ["break crane","change lamp"],
                    "requirement": {"pasatigi",'lamp'},
                    "requirement time": "2:00 PM"
                },

                {
                    "adress": "metalistiv 3",
                    "task" : ["break crane","check gase"],
                    "requirement": {"pasatigi","overtka","key of 27"},
                    "requirement time": "12:00 PM"
                }
            ]
     },
    {
        "master_name":"Georg",
        "work_diary":
            [


                    {
                        "adress": "polythnichna 1",
                        "task" : ["break crane",'change windows','connect to internet'],
                        "requirement": {"key of 18","otvertka","paialnmik"},
                        "requirement time": "10:00 AM"
                    },


                    {
                        "adress": "polythnichna 6",
                        "task" : ["break crane","change lamp"],
                        "requirement": {"pasatigi",'lamp'},
                        "requirement time": "2:00 PM"
                    },


                    {
                        "adress": "polythnichna 2",
                        "task" : ["break crane","check gase"],
                        "requirement": {"pasatigi","overtka","key of 27"},
                        "requirement time": "12:00 PM"
                    }
             ]

         }
]

def adress_1(ds):
    if ds == []:
        return
    row = ds[0]
    print(row["adress"])

    adress_1(ds[1:])


def adress_(ds):
   if ds == []:
      return
   row = ds[0]
   work_diary = row["work_diary"]
   print(row["master_name"])
   adress_1(work_diary)
   adress_(ds[1:])



def task_lenght():
    print('task_lenght')
    for master_work in work_plan:
        task_lenght_ = 0
        mastr_name = master_work['master_name']
        for work in master_work['work_diary']:
            task_lenght_+= work['task'].__len__()
        print("mastr_name",mastr_name)
        print('task_lenght',task_lenght_)


if __name__ == '__main__':
    task_lenght()
    print('adress_')
    adress_(work_plan)#