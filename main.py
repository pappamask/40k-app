import streamlit as st
from PIL import Image
from killTeamData import *
from dataCards import *

im = Image.open('sally.ico')
st.set_page_config(
    page_title='Grimdank app for kill team scout squad',
    layout='wide',
    initial_sidebar_state='expanded',
    page_icon=im,
    menu_items=None
)

#### Faction rules ####
with st.sidebar.expander('FACTION RULES'):
    st.title('FORWARD SCOUTING')
    redeploy = st.checkbox('Redeploy (1)', 
        help=redeploy_text)
    reposition = st.checkbox('Reposition (2)',
        help=reposition_text)
    trip_alarm = st.checkbox('Trip Alarm (2)',
        help=trip_alarm_text)
    booby_trap = st.checkbox('Booby Trap (1)',
        help=booby_trap_text)
    diversion = st.checkbox('Diversion (1)',
        help=diversion_text)
    devise_plan = st.checkbox('Devise Plan (1)',
        help=devise_plan_text)
    designate_target = st.checkbox('Designate Target (1)',
        help=designate_target_text)
    spy = st.checkbox('Spy (1)',
        help=spy_text)
    tactical_manoeuvre = st.checkbox('Tactical Manoeuvre (1)',
        help=tactical_manoeuvre_text)

#### Faction equipment ####
with st.sidebar.expander('FACTION EQUIPMENT'):
    camo_cloak = st.checkbox('Camo Cloak')
    targeting_oculars = st.checkbox('Targeting Oculars')
    blades_and_knives = st.checkbox('Combat blades and knives')
    heavy_weapon_bipod = st.checkbox('Heavy Weapon Bipod')

#### Universal equipment ####
with st.sidebar.expander('UNIVERSAL EQUIPMENT'):
    portable_barricade = st.checkbox('Portable Barricade')
    if portable_barricade:
        no_portable_barricade = st.number_input('Number of Portable Barricades: ', min_value=1, step=1)
        
    utility_grenades = st.checkbox('Utility Grenades')
    ammo_cache = st.checkbox('Ammo Cache')
    if ammo_cache:
        no_ammo_cache = st.number_input('Number of Ammo Caches: ', min_value=1, step=1)
    


with st.expander('PLOYS'):
    col1, col2 = st.columns(2)
    with col1:
        st.header('STRATEGY PLOYS')
        with st.container(border=True):
            st.markdown(guerilla_engagement_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(gunfire_ambush_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(blade_ambush_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(stealth_relocation_text, unsafe_allow_html=True)    
        
    with col2:
        st.header('FIREFIGHT PLOYS')
        with st.container(border=True):
            st.markdown(astartes_training_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(raw_physiology_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(emboldened_aspirant_text, unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown(covert_position_text, unsafe_allow_html=True)    
        
        
#### UNITS ####
with st.expander('DATACARDS'):
    with st.container(border=True):
        st.markdown(scout_sergeant, unsafe_allow_html=True)
        
    with st.container(border=True):
        st.markdown(scout_heaver_gunner, unsafe_allow_html=True)