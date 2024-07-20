import streamlit as st
st.title('Next Prime Number')
def isprime(n):
    prime=True
    if n<=1:
        prime =False
    else:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                prime=False
                break
    return prime
input_num1=st.number_input("Insert a number", value=None, placeholder="Type a number...",min_value=0)

# input_num1=int(input())
if st.button('Next Prime'):
    input_num=input_num1
    if input_num==None:
        st.subheader('Please, Input a Number')
    elif isprime(input_num):
        input_num+=1
        while isprime(input_num) == False:
            input_num+=1
        # print(f'The next prime number of {input_num1} is: {input_num}')
        # st.subheader(f'The next prime number of {input_num1} is: {input_num}')
        st.subheader(f'The next prime number of :blue[{input_num1}] is: :blue[{input_num}]')
    else:
        while isprime(input_num) == False:
            input_num+=1
        # print(f'The next prime number of {input_num1} is: {input_num}')
        # st.subheader(f'The next prime number of {input_num1} is: {input_num}')
        st.subheader(f'The next prime number of :blue[{input_num1}] is: :blue[{input_num}]')