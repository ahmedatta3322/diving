import React, { Component } from 'react'
import { Button , Box , Container , Notification , Card , CardHeader , CardHeaderTitle , CardHeaderIcon , Icon , CardImage , CardContent , Media , MediaLeft , MediaContent , Title , Subtitle , Content , Image , Columns, Column } from "bloomer"

export default class Divers extends Component {
    state = {
        data: []
    }

    componentDidMount() {
        fetch("/divers").then(
            (response) => {
                if (response.status !== 200) {
                    console.log('Looks like there was a problem. Status Code: ' +
                        response.status);
                }
                return response.json();
            }).then(
            (data) => {
                this.setState({
                    data: data
                })
            }
        )
    }
    render() {
        console.log(Object.values(this.state.data))
        console.log(typeof (this.state.data))
        return (
            <Container>
                <Columns isCentered isMultiline	>
            {Object.values(this.state.data).map((el) => {
                    return (
                    <Column isSize='1/4'>
                    <Card>
                    <CardHeader>
                        <CardHeaderTitle>
                            Diver card
                        </CardHeaderTitle>
                        <CardHeaderIcon>
                            <Icon className="fa fa-angle-down" />
                        </CardHeaderIcon>
                    </CardHeader>
                    <CardImage>
                        <Image isRatio='4:3' src={ el.photo } />
                    </CardImage>
                    <CardContent>
                        <Media>
                            <MediaLeft>
                                <Image isSize='48x48' src='https://via.placeholder.com/96x96' />
                            </MediaLeft>
                            <MediaContent>
                                <Title isSize={4}>{ el.name }</Title>
                                <Subtitle isSize={6}>@John Wick</Subtitle>
                            </MediaContent>
                        </Media>
                        <Content>
                            Dive Master 
                            <br/>
                            <small>11:09 PM - 30 October 2014</small>
                        </Content>
                    </CardContent>
                </Card>
                    </Column>
                )
                    })   }
                    </Columns>
                    </Container>
        )
        
    }
}