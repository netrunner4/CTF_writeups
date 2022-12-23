# rev/Gimi's Wonderland

### Description
> On his way to buy a new RTX as a Christmas gift Gimi had an altercation with the ender dragon and had to spend a substantial amount of money on (duped) notch apples. Fortunately, he stumbled upon an IT enthusiast who offered him a discount voucher in exchange for homework help. In a hurry, Gimi outsources the job to you in exchange for a flag. Help them, save the day!

We are given a minecraft map and a mod for NPCs for minecraft 1.12.2

On map we have NPC with 2 pages of code and a redstone circuit behind him

On first page there is `init` function which takes our messages from chat as a **flag** and sets **rkey** at 143
```javascript
function init(e)
{
    e.npc.say("Interrupt request handler online!");
    //Lets listen to the 'playerChat' event
    eventBus().on('playerChat', function(chatEvent, otherArgument)
    {  
        //e.npc.say(chatEvent.message);
        e.npc.say("Roger");
        var world = e.npc.getWorld();
        var tempdata = world.tempdata;
        tempdata.put("flag", chatEvent.message);
        tempdata.put("rkey", 0x8f);
    }, e.npc.UUID); //Unique ID to avoid registering same functions!
}
```
Then we have `to_bits` function. In mode 0 it changes **rkey** by **x** and converts **x** in binary represented by redstone blocks without offset. In mode 1 it sets offset and converts **x** to restone blocks
```javascript
function to_bits(world, x, mode)
{
    var offset = 0;
    if (mode != 0)
    {
        offset =2;
    }
    
    else
    {      
        var tempdata = world.tempdata;
        var old_rkey = tempdata.get("rkey");
        tempdata.put("rkey", (x + old_rkey) & 0xFF);
        print("Setting rkey " + ((x + old_rkey) & 0xFF));
    }
    
    for (var i = 0; i < 8; i++)
    {
        if (x & (1<<i))
        {
            world.setBlock(-291 + 4 * i + offset, 4, 629, "minecraft:redstone_block", 0);
        }
        else
        {
            world.setBlock(-291 + 4 * i + offset, 4, 629, "minecraft:wool", 14);
        }
    }
}
```

Here are the blocks changed by `to_bits` function. In every two block pair left is changed in mode 0 and right is changed in mode 1
![Image with redstone and wool blocks from a circuit](/images/circuit_redstone.png)

Next function is `from_bits`. It reads 4 groups of 7 redstone lamps and converts them into letters using dictionary. Then the letters are added to **encflag**
```javascript
function from_bits(world)
{
    var xstart = -311;
    var tempdata = world.tempdata;
    var dict = {
    36: 'A',
    206: 'C',
    236: 'G',
    246: 'T'
    }
    
    if (tempdata.has("encflag"))
    {
        for(var i = 0; i < 4; i++)
        {
            var num = 0;
            for(var j = 0; j < 7; j++)
            {
                var x = xstart + 20 * i + 2 * j;
                var bl = world.getBlock(x, 4, 691).getName();
                if(bl == "minecraft:lit_redstone_lamp")
                {
                    num = num + 1;
                }
                num = num << 1;
            }
            tempdata.put("encflag", tempdata.get("encflag") + dict[num]);
        }
    }
    
    else
    {
        tempdata.put("encflag", "");
    }
}
```
This is one block of lamps (1110110) which is letter G. Other combinations are 0010010-A, 1100111-C, 1111011-T
![Image with one block of redstone lamps from a circuit](/images/circuit_lamps.png)

After some tests we can find that each letter takes two input signals and each signal consists of pair of redstone/wool block with and without offset. 00 signal results in T, 01 in C, 10 in A and 11 in G. Two last letters are mirrored so they have 01 for A and 10 for C

Last function is `tick`. It takes **flag** from out message and encodes each letter into four A/T/G/C using letter as **x** in `to_bits` function mode 0 and **rkey** as **x** in `to_bits` function mode 1. Then it compares **encflag** with hardcoded string
```javascript
function tick(event)
{
    var world = event.npc.getWorld();
    var tempdata = world.tempdata;
    
    if(((world.getTime() / 10) >> 0 )% 5 != 0)
    {
        return;
    }
    
    if (tempdata.has("flag"))
    {
        from_bits(world);
        var flag = tempdata.get("flag");
        if (flag.length == 0)
        {
            event.npc.say("Your champion gene is: " + tempdata.get("encflag"));
            //event.npc.say("rkey: " + tempdata.get("rkey"));
            
            if(tempdata.get("encflag") != "GACGCCTGACCCTTATATGGCGTATCCTTGAGCGGCCCCTAAGATCCCTCAGGGGTTTACGCGGAGACCTCTCAAAGGGTGGTGGCCCCTCAGCGAAGATCGAGTGGCAGCTGTCATGACGATTCATAGGATCCAGACTAGGCCATGA")
            {
                event.npc.say("Unfortunately, that's not what i'm looking for!");
            }
            else
            {
                event.npc.say("Thanks, you found it!");
            }
            
            print(tempdata.get("encflag"));
            tempdata.remove("flag");
            tempdata.remove("encflag");
        }
        
        else
        {
            var num = flag.charCodeAt(0);
            var chr = flag.substr(0, 1);
            to_bits(world, tempdata.get("rkey"), 1);
            to_bits(world, num, 0);
            event.npc.say("Processing " + chr);
            tempdata.put("flag", flag.substr(1));
        }
    }
}
```

So we have encoded letters and **rkey**. Having them we can find **x** by getting required signal sequence for quartet of A/T/G/C letters and then figuring out redstone/wool blocks without offset (blocks with offset is binary representation of **rkey**) needed to get this sequence

Let's get the first letter. First 4 encoded letters are GACG. It is 11 10 10(mirrored) 11 in signals. **rkey** is 143 so blocks with offset are 10001111

With **x**=0 we get signals 11 11 00 01
![Image with redstone and wool blocks from a circuit where rkey set to 143](/images/circuit_redstone_143.png)

So we need to change fourth, fifth and seventh block
![Image with redstone and wool blocks from a circuit where rkey set to 143 and x set to 88](/images/circuit_redstone_143_88.png)

Now we can find out **x** from changed blocks: 64+16+8=88 what is letter X. And then we can add this number to old **rkey** to get a new one - 143+88=231 (also new rkey is written to logs of NPC with every letter encoded)

Then we repeat this process with next 4 encoded letters and so on

In result our **flag** is *X-MAS{h4rdWar3_encrypt1on_laNGuagE}..*
