import streamlit as st
from PIL import Image

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
        help='''Change the set up of one third of your operatives
        (rounding up).''')
    reposition = st.checkbox('Reposition (2)',
        help='''Perform a free Reposition action with one friendly operative  
that’s wholly within your drop zone. It must end that move  
wholly within 3" of your drop zone.''')
    trip_alarm = st.checkbox('Trip Alarm (2)',
        help='''Place one of your Trip Alarm markers more than 6" from your  
opponent’s drop zone. During the first and second turning  
point, whenever a friendly SCOUT SQUAD operative is  
shooting an enemy operative that’s within 2" of that marker,  
that friendly operative’s ranged weapons have the Seek  
weapon rule. In the Ready step of the third Strategy phase,  
remove that marker.''')
    booby_trap = st.checkbox('Booby Trap (1)',
        help='''Place one of your Booby Trap markers more than 6" from your  
opponent’s drop zone and more than 2" from other markers,  
access points and Accessible terrain. The first time your  
Booby Trap marker is within an enemy operative’s control  
range, remove that marker and inflict 2D3 damage on that  
operative; if it isn’t incapacitated, end its action (if any), even  
if that action’s effects aren’t fulfilled. If it cannot be placed,  
move it the minimum amount to do so.''')
    diversion = st.checkbox('Diversion (1)',
        help='''Once per battle STRATEGIC GAMBIT. Select one enemy   
operative within 6" of a killzone edge. Until the end of that  
operative’s next activation, subtract 1 from its APL stat.''')
    devise_plan = st.checkbox('Devise Plan (1)',
        help='''You gain 1CP.''')
    designate_target = st.checkbox('Designate Target (1)',
        help='''Select one enemy operative to gain one of your Target tokens.  
Whenever a friendly SCOUT SQUAD operative is shooting  
against, fighting against or retaliating against an enemy  
operative that has one of your Target tokens, you can re-roll  
one of your attack dice.''')
    spy = st.checkbox('Spy (1)',
        help='''Approved Ops only. Your opponent must reveal their selected  
tac op.''')
    tactical_manoeuvre = st.checkbox('Tactical Manoeuvre (1)',
        help='''Once per battle STRATEGIC GAMBIT. Select one friendly  
operative. Until the end of that operative’s next activation, add  
1 to its APL stat.''')

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
            st.markdown('''
:violet-background[GUERRILLA ENGAGEMENT]\n
            
<small>_Space Marine Scouts learn to use terrain to their advantage,
preventing the enemy from getting a bead on them as they move within
killing range._</small>
            
Whenever an enemy operative is shooting a friendly SCOUT
SQUAD operative, if that friendly operative is in cover and
more than 6" from enemy operatives it’s visible to, you can
re-roll one of your defence dice
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:violet-background[GUNFIRE AMBUSH]\n
            
<small>_Scout Squads utilise stealth to close within range of their foes, carefully
select their targets and unleash a devastating barrage of bolt rounds and
shotgun slugs._</small>
            
Whenever a friendly SCOUT SQUAD operative is shooting
during its activation, if its order was changed from Conceal
to Engage at the start of that activation, or it wasn’t visible to
enemy operatives at the start of that activation:
 - That friendly operative’s ranged weapons have the
Balanced weapon rule.
 - If the target is expended, that friendly operative’s ranged
weapons have the Ceaseless weapon rule instead.
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:violet-background[BLADE AMBUSH]\n
            
<small>_At times when stealth is of the utmost importance, the blade is
preferable to the bolter, and just as deadly._</small>
            
Whenever a friendly SCOUT SQUAD operative is fighting
during its activation, if its order was changed from Conceal
to Engage at the start of that activation, or it wasn’t visible to
enemy operatives at the start of that activation:
 - That friendly operative’s melee weapons have the Ceaseless
weapon rule.
 - If the target is expended, that friendly operative’s melee
weapons also have the Rending weapon rule.
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:violet-background[STEALTH RELOCATION]\n
            
<small>_Space Marine Scout Squads are highly mobile units, shifting swiftly from
cover to cover in order to outmanoeuvre the foe._</small>
            
Select one friendly SCOUT SQUAD operative more than
6" from enemy operatives. That friendly operative can
immediately perform a free Dash action and/or you can
change its order. 
                        ''', unsafe_allow_html=True)    
        
    with col2:
        st.header('FIREFIGHT PLOYS')
        with st.container(border=True):
            st.markdown('''
:red-background[ASTARTES TRAINING]\n
            
<small>_Space Marine Scouts learn to use terrain to their advantage,
preventing the enemy from getting a bead on them as they move within
killing range._</small>
            
Whenever an enemy operative is shooting a friendly SCOUT
SQUAD operative, if that friendly operative is in cover and
more than 6" from enemy operatives it’s visible to, you can
re-roll one of your defence dice
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:red-background[RAW PHYSIOLOGY]\n
            
<small>_Scout Squads utilise stealth to close within range of their foes, carefully
select their targets and unleash a devastating barrage of bolt rounds and
shotgun slugs._</small>
            
Whenever a friendly SCOUT SQUAD operative is shooting
during its activation, if its order was changed from Conceal
to Engage at the start of that activation, or it wasn’t visible to
enemy operatives at the start of that activation:
 - That friendly operative’s ranged weapons have the
Balanced weapon rule.
 - If the target is expended, that friendly operative’s ranged
weapons have the Ceaseless weapon rule instead.
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:red-background[EMBOLDENED ASPIRANT]\n
            
<small>_At times when stealth is of the utmost importance, the blade is
preferable to the bolter, and just as deadly._</small>
            
Whenever a friendly SCOUT SQUAD operative is fighting
during its activation, if its order was changed from Conceal
to Engage at the start of that activation, or it wasn’t visible to
enemy operatives at the start of that activation:
 - That friendly operative’s melee weapons have the Ceaseless
weapon rule.
 - If the target is expended, that friendly operative’s melee
weapons also have the Rending weapon rule.
                        ''', unsafe_allow_html=True)
            
        with st.container(border=True):
            st.markdown('''
:red-background[COVERT POSITION]\n
            
<small>_Space Marine Scout Squads are highly mobile units, shifting swiftly from
cover to cover in order to outmanoeuvre the foe._</small>
            
Select one friendly SCOUT SQUAD operative more than
6" from enemy operatives. That friendly operative can
immediately perform a free Dash action and/or you can
change its order. 
                        ''', unsafe_allow_html=True)    
        
        
#### UNITS ####
with st.expander('DATACARDS'):
    with st.container(border=True):
        st.write('Sergeant bob')