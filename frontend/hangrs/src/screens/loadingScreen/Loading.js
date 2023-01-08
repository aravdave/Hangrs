import React, { component } from 'react'
import { View, Text, StyleSheet, Animated } from 'react-native'



export default function Loading() {

    return (
        <View style = {styles.container}>
            <Text style = {styles.logoText}>hangrs</Text>
        </View>

    )


}

const styles = StyleSheet.create({
    container: {
        flex:1,
        backgroundColor:'black',
        justifyContent:'center',
        alignItems:'center',
    },
    logoText:{
        color:'white',
        fontFamily: 'GoogleSans-Bold',
        fontSize: 60,
        fontWeight:'900',
    }
})
