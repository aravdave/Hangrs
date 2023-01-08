import {
  StyleSheet,
  View,
  Text,
  Alert,
  TextInput,
  FlatList,
} from 'react-native';
import Header from './src/components/Header.js';
import React from 'react';
import SignInScreen from './src/screens/signinscreen/index.js';
import SignUpScreen from './src/screens/SignUpScreen/SignUpScreen.js';
import WelcomeScreen from './src/screens/WelcomeScreen/WelcomeScreen.js';

function App(){
  return(
    <View style={{flex:1}}>
      <WelcomeScreen />
    </View>
  )
}

export default App;
