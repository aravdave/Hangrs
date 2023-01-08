import React, { component } from 'react'
import { View, Text, StyleSheet, Image, Animated } from 'react-native'
import account from '../../assets/account.jpg'
import cart from '../../assets/cart.png'

export default function Header() {

    return (
        <View style = {styles.container}>
            <Image source={account} style = {styles.profile}/>
            <View style = {styles.textContainer}>
                <Text style = {styles.text}>hangrs</Text>
            </View>
            <Image source = {cart} style = {styles.profile}/>
        </View>

    )


}

const styles = StyleSheet.create({
    container: {
        paddingTop: 9,
        height:'10%',
        backgroundColor:'black',
        flexDirection: 'row',
        alignItems: 'center',
    },
    profile:{
        width:30,
        height: 30,
        resizeMode: 'contain',
        flex: 1,
    },
    text:{
        color:'white',
        fontFamily: 'GoogleSans-Bold',
        fontSize: 35,
        fontWeight:'900',
        flex: 5,
    },
    textContainer:{
        flex: 5,
        alignItems:'center',
    }
})
