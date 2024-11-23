import streamlit as st
from utils.utils import update_page_state


def main(team): 
    with team.container():
        st.balloons()
        st.write("""<br><center><h2>Meet the Team</h2></center><br>""", unsafe_allow_html=True)

        a,_,b = st.columns([1.5,0.2,3])
        
        with open("assets/contributors.txt", "r") as f:
            contributors = f.read().split('---')
        
        with a.container(border=True):
            st.write(f"<br><br><br><center><h4>Chapter Lead</h4><p>Arpit Sengar</p></center>",unsafe_allow_html=True)
            st.write(f"<center><h4>Chapter Co-Lead</h4><p>Rohit Dwivedi</p></center><br><br><br>",unsafe_allow_html=True)
        
        with b.container(border=True):
            st.write(f"<br><center><h4>Contributors</h4></center><br>",unsafe_allow_html=True)
            cols = st.columns([0.5,2,2,2,0.5])
            
            for idx, col in enumerate(cols[1:4]):
                with col:
                    st.write(f"<center><p>{contributors[idx]}</p></center>",unsafe_allow_html=True)
            
            st.write("<br>" * 2, unsafe_allow_html=True)