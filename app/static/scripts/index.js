console.log('loaded script');

    
function createAlpaca () {

    const data = {
        id = '15',
        name: 'Julian Orchestra',
        displayName: 'Jules',
        bio: "'let's party'",
        age: '22',
        hobbies: ['music','games', 'producing', 'hockey', 'mixing'],
        contact: {'phoneNumber': '604-728-4671', 'email': 'julianborochoa@gmail.com'},
        sex: 'female',
    }

    fetch(
        "/create",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("successful post", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );

}

function deleteAlpaca () {
    const data = {
        id = '1',
        name = 'Fred',
        displayName = 'Fred The Menace',
        bio = "'I am super athletic, love benching weights. In my spare time when I am not gaining muscle, I love going to the gym. Other alpaca's want to be me'",
        age = '21',
        hobbies = ['Gym', 'Hikes', 'Running', 'Talking about my abs'],
        contact = {'phoneNumer' : '203-123-0987', 'email' : 'fred@gym.com'},
        sex = 'male'
    }

    fetch(
        "/delete",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    ).then(
        (response) => {
            return response.json();
        }
    ).then(
        (json) => {
            console.log("successful post", json);
            const message = json.message
            window.alert(message)
        }
    ).catch(
        (error) => {
            console.error("error", error);
        }
    );
}

