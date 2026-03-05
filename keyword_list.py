

#Hypersexualize theme
hypersexualize_f = { 'bra', 'lingerie', 'teddy','slut',
'whore','bitch', 'jezebel', 'mistress',
 'breast', 'cougar'}

hypersexualize_m = {'boxers', 'womanizer', 'penis', 'sperm'}
hypersexualize_n = {'flaunt', 'appeal', 'reveal', 'underwear',
'sex', 'teas',  'lur', 'entic', 'flirt',
'seduc', 'affair', 'adulter', 'promiscu', 'charm',
'sexy', 'glamour', 'attractive','ass', 'booty', 'oversexed',
'appeal', 'reveal', 'sex', 'sexy', 'sexual', 'tease',
'teasing', 'lure','luring','lured', 'entice', 'enticing', 'enticed',
 'flirt',  'flirtatious',  'seduce','promiscuity', 'promiscuous',
'charm', 'glamour', 'slut', 'adulterer', 'adulter',
'relationship', 'intercourse','sexually', 'romantic',
'cheat', 'whore', 'unfaith', 'infidel', 'lust'}
hypersexualize_theme = hypersexualize_f | hypersexualize_m | hypersexualize_n


#split into parenting positive and parenting negative
parenting_f={ 'mother', 'matriarch', 'stepmother', 'mom'}
parenting_m ={ 'father', 'patriarch', 'stepfather', 'dad'}
parenting_neutral = {'child','therapy',' minor', 'parents',
 'therapist',  'kids', 'children',
  'school', 'house', 'home',
  'sister', 'family', 'disciplinarian', 'household','caretak'}
parenting_pos ={  'family oriented', 'caring', 'nurture','respect','foster'}
parenting_neg = {'child abuse', 'negligent','neglect', 'estrang'}
parenting_theme= parenting_f |parenting_m | parenting_pos | parenting_neg


pathologizing_theme = {'calculated', 'cold', 'inhuman', 'unnatural',
 'unstable',  'fake', 'deranged','tears',
 'unemotional', 'liar', 'malinger', 'uncontrollable',
  'angry', 'insincere', 'unempathetic', 'lie',
  'liar','irrational','scheme','cry',
  'manipulate','irrational', 'hysterical', 'hysteria',
   'hysteri', 'deceit', 'thief', 'cheat','exaggerate', 'pretend' }

sexuality_f = {'bitch', 'dyke', 'butch','lesbian'}
sexuality_m = {'gay', 'punk'}
sexuality_n = {'bisexual', 'queer'}
sexuality_theme = sexuality_f | sexuality_m | sexuality_n

# perhaps split into adhering to gender roles and not adhering ?
gender_f = {'maternal','feminine','wife','lady', 'woman','housewife'}
gender_m= {'masculine', 'manly','man', 'paternal', 'husband', }
gender_role_neg = {'cold',
'uncaring', 'unfriendly', 'unemotional',
'abandonment', 'neglect','selfish', 'unnatural',
'assertive','ugly', 'aggressive',
'confrontational', 'violent', 'unfeeling',
'child abuse','emotionally abusive',
'materialistic', 'selfish', 'self centered',
'callou'
}
gender_role_pos = {'nurture', 'homemaker', 'virgin',
'pure', 'sacrificial','family oriented', 'physically attractive',
'sexual appeal', 'sex appeal' , 'caring', 'friendly', 'emotional', }
gender_roles_theme =gender_f | gender_m | gender_role_neg | gender_role_pos


discredit_theme = {'liar', 'lie', 'unbelievable',
'unreliable', 'inconsistent','corroborate', 'atypical',
 'asking for it','asked for it',
 'deceit', 'cheat', 'deceiv',
 'exagger', 'untru', 'manipulat',
 'thief','pretend', 'despic', 'dishonest', 'stupid', 'fool'}

immigration = {'infiltrat', 'alien', 'foreign',
'backward','citizenship',
'illegal', 'dirty','untrustworthy','
exotic', 'diverse', 'different',
'ethnic','accent', 'english', 'custom',
'culture','steal',  'infiltrat'}

drugs_addiction = { 'cocaine', 'speed', 'marijuana',
 'heroin', 'addict', 'drug',
  'methamphetamine', 'brain', 'meth' ,
  'influence','nanograms' ,'alcohol' ,
  'stimulant','valium', 'crack' ,
  'crystal','gram', 'crack house',
'addict', 'addiction','snort','dealer'
'lsd', 'amphetamin'}

racial_tropes_words = {'negro', 'feral', 'lazy',
'brute','angry', 'untamable', 'gang',
'lazy', 'welfare', 'savage', 'animal',
'belligerent',  'thug',
'culture', 'customs', 'diverse','foreign', 'exotic',
  'accent', 'steal', 'english',
  'foreign', 'backward', 'community', 'infiltrat'
  'dirty', 'ethnic', 'taking over'}
racial_tropes_f = {'mammy', 'matriarch', 'welfare queen'}
racial_tropes_m = {'patriarch', 'deadbeat dad'}
racial_tropes_black = {'negro',  'lazy',
'brute','angry', 'untamable', 'gang',
'lazy', 'welfare', 'savage', 'animal',
'belligerent', 'thug' }
racial_tropes_latine = {'lazy', 'gang', 'welfare',
'culture', 'customs', 'infiltrate'
 'diverse','foreign', 'exotic',
  'accent', 'steal', 'english',
  'foreign', 'backward', 'community',
  'dirty', 'ethnic', 'taking over'}


racial_tropes_theme = racial_tropes_n | racial_tropes_f | racial_tropes_m |racial_tropes_black |racial_tropes_latine

poverty = {'poor', 'welfare', 'poverty',
'lazy', 'cheap', 'dirty', 'disorganized',
 'messy', 'greedy', 'materialistic',
  'acquisitive','motel', 'food stamps',
   'contribution to society', 'trailer trash'}

mental_health_theme = {'disorder', 'mental', 'depression',
 'bipolar', 'antisocial' , 'disorders',
 'criteria' ,'manic' ,'lithium', 'prozac' ,
 'medication' ,'psychosis', 'prednisone' ,
 'xanax' ,'prescribed', 'effects',
 'battered woman' , 'domestic',
'syndrome', 'abuse', 'iq', 'performance',
'average', 'brain' ,'impairment' ,'functioning',
 'disability' ,'learning','diagnosis',
  'brain', 'mental', 'symptoms',
  'malingering', 'antisocial', 'crazy'}


themes = {'Hypersexualizing': hypersexualize_theme,
          'Discrediting' : discredit_theme,
          'Pathologizing': pathologizing_theme,
          'Parenting' :parenting_all,
          'Gender and Gender Roles': gender_roles_theme,
          'Sexuality': sexuality_theme,
          'Racial Tropes': racial_tropes_theme,
          'Immigration': immigration,
          'Drugs and Addiction': drugs_addiction,
          'Poverty': poverty,
          'Mental Health' : mental_health_all}
subthemes = {"Gender and Gender Roles_positive":gender_role_pos,
"Gender and Gender Roles_negative": gender_role_neg,
'Racial Tropes_Black':racial_tropes_black,
'Racial Tropes_Latine':racial_tropes_latine,
"All Feminine Keywords": racial_tropes_f |parenting_f | sexuality_f | hypersexualize_f |gender_f,
"All Masucline Keywords": racial_tropes_m |parenting_m | sexuality_m | hypersexualize_m |gender_m
}
