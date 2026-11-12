def extract_surname(name):
    parts = name.split()
    if len(parts) > 1:
        return parts[-1]  # Assuming the last word is the surname
    else:
        return None  # Indicate no surname


voter_names = [
    "Vineet Kumar", "Nitin Kumar", "Utkarsh Kumar", "Sri Chand", "Sneh Lata",
    "Chamel Singh", "Sunita Devi", "Natasha", "Nidhi", "Robin Sing",
    "Dhyan Singh", "Hardev Singh", "Archana Devi", "Lalita", "Nardev",
    "Mohit Chawla", "Akshit Chawla", "Harnam Singh", "Naresh Kumar", "Susham Lata",
    "Mamta Devi", "Namit Chawla", "Viso Devi", "Bidhi Singh", "Kanta Devi",
    "Ashok Kumar", "Manoj Kumar", "Ranjana Kumari", "Sunil Kumar", "Meena Kumari",
    "Naveen Kumar", "Anu Wala", "Maninder Singh", "Jyoti Wala", "Ankur Chawla",
    "Ankita Chawla", "Khushboo", "Muskan Chawla", "Jaswinder", "Jagga",
    "Praveen", "Suresh", "Aruna", "Milkhi Ram", "Madan Lal",
    "Raj Kumar", "Kamlesh Kumari", "Shamsher Singh", "Neelma Devi", "Devi Lal", "Sunita Devi",
    "Santosh Kumari", "Nishant Kumar", "Deept Chaudhary", "Ankit", "Rohit Chaudhary", "Puran Chand",
    "Sureshta Devi", "Subhash Chand", "Kumari Sapna", "Jeevan Lal", "Sarita Devi", "Priyanka",
    "Prince", "Roshan Lal", "Simro Devi", "Rakesh Kumar", "Sudha Kumari", "Naveen Kumar",
    "Kajal", "Rama Devi", "Saroj Kumari", "Kushal Kumar", "Mathra Devi", "Suresh Kumar",
    "Joginder Pal", "Krishna Devi", "Kanta Devi", "Manish Kumar", "Anish Kumar", "Anil Kumar",
    "Vishali Devi", "Kishori Lal", "Chaichla Devi", "Sakshi", "Neelam Kumari", "Pritam Chand",
    "Soma Devi", "Ajay Kumar", "Jeevan Lal", "Raj Kumari", "Sanjay Kumar", "Varsha",
    "Kewal Krishan", "Sonu Devi", "Sajan", "Kajal", "Suraj", "Sneh Lata",
    "Ram Saran", "Shanti Devi", "Krishan Kumar", "Darshana Devi", "Vinod Kumar", "Baby",
    "Rajat Kumar", "Anjali", "Shakuntala Devi", "Rakesh Kumar", "Rabinder Kumar", "Vindo Devi",
    "Meena Kumari", "Jaswant", "Darshana", "Jitendra Kumar", "Monika", "Komal",
    "Nirmala", "Anup Singh", "Saroop Singh", "Anita", "Ashok Kumar", "Seema",
    "Swati", "Sameer", "Bima Devi", "Raj Kumar", "Ranjana Devi", "Urmila Devi",
    "Rajinder Kumar", "Rekha Devi", "Rakesh Kumar", "Sapna Devi", "Balbir Singh", "Sunita Devi",
    "Amit Kumar", "Sunil Kumar", "Aarti", "Shilpa", "Naveen Kumar", "Babu Lal",
    "Krishna Devi", "Swarn Kanta", "Manisha Kumari", "Mandeep Singh", "Akshay Kumar", "Om Raj",
    "Sunita Devi", "Pawan Kumar", "Rakesh Kumar", "Manohar Lal", "Ramna Devi", "Anju",
    "Anjana", "Rajat Kumar", "Manish Kumar", "Sakshi", "Ishul Kuthiyala", "Tamanna Devi",
    "Satya Devi", "Amit Kumar", "Monika", "Vandana Rani", "Shiv Dutt", "Nisha Rani",
    "Pankaj Kumar", "Praveen Kumari", "Saina Devi", "Arvind Kumar", "Babli", "Ramesh Kumar",
    "Vijay Kumari", "Rajesh Kumar", "Pankaj Sharma", "Gyan Singh", "Nirmala Devi", "Pawan Kumar",
    "Joginder Singh", "Rajinder Singh", "Ashok Kumar", "Rajni Devi", "Pooja Devi", "Suman Devi",
    "Rahul", "Harish Kumar", "Vishal Kumar", "Suresh Kumar", "Shreshta Devi", "Sunita Devi",
    "Shivani Devi", "Preeti", "Anshul Dadwal", "Mahindra Singh", "Sandla Devi", "Parveen Kumar",
    "Jeevan Kumar", "Rekha Devi", "Priyanka", "Kartar Chand", "Sarla Devi", "Sanjay Kumar",
    "Pradeep Singh", "Krishan Kumar", "Mohan Lal", "Manmeet Singh", "Anjana Devi", "Madan Lal",
    "Neeta Kumari", "Surjeet Singh", "Harish Dadwal", "Nirmala Devi", "Kartar Singh", "Praveena Devi",
    "Nitesh Kumar", "Ria", "Bharti", "Satya Devi", "Iqbal Singh", "Reena Kumari",
    "Dipanshu", "Dipali", "Pooja Karel", "Avtar Singh", "Kamlesh Kumari", "Sanni Panjala",
    "Atul", "Vashla Devi", "Sita Devi", "Munish Kumar", "Meenakshi Dekha", "Jasdev Singh",
    "Bina Devi", "Sanjay Kumar", "Abhishek", "Devinder Singh", "Mahindra Kaur", "Raghubir Singh",
    "Satveer Kaur", "Deepak Kumar", "Pradeep Kumar"
]

surnames = [extract_surname(name) for name in voter_names]

# Remove None values (names without surnames)
surnames_only = [surname for surname in surnames if surname is not None]

# Get unique surnames
unique_surnames = list(set(surnames_only))

# Print the list of surnames
print("List of surnames:", unique_surnames)